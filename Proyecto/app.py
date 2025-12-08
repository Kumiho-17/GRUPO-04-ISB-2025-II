from flask import Flask, render_template, request, redirect, url_for, send_file
import numpy as np
from datetime import datetime
from io import BytesIO
from reportlab.lib.utils import ImageReader 
import matplotlib.pyplot as plt             


# ----------------------------------------------
# MODELOS / FILTROS / PREPROCESAMIENTO
# ----------------------------------------------
from scipy.signal import butter, filtfilt, iirnotch
from tensorflow.keras.models import load_model

app = Flask(__name__)

# ---------------------------------------------------
# CONFIGURACIÓN GENERAL
# ---------------------------------------------------
GESTURE_LABELS = {
    0: "Open bottle (tripod grasp)",
    1: "Lateral grasp",
    2: "Parallel extension grasp",
    3: "Power grasp"
}

MODEL_DISPLAY = {
    "cnn_mejorada": "CNN mejorada – Ventanas crudas (200×10, capa latente 64-D)"
}

PATIENT_HISTORY = {}
CURRENT_PATIENT = None

FS = 2000
N_CHANNELS = 10
WINDOW_SIZE = 400
OVERLAP = 0.5


# ---------------------------------------------------
# CARGAR MODELO CNN MEJORADA
# ---------------------------------------------------
from tensorflow.keras.models import load_model
import os

print("📡 Intentando cargar modelo cnn_mejorada.h5 ...")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "cnn_mejorada.h5")

try:
    CNN_MODEL = load_model(MODEL_PATH)
    print(f"✅ Modelo cargado correctamente desde: {MODEL_PATH}")
except Exception as e:
    CNN_MODEL = None
    print("❌ ERROR: No se pudo cargar cnn_mejorada.h5")
    print("   Ruta intentada:", MODEL_PATH)
    print("   Motivo:", e)


# ---------------------------------------------------
# PACIENTES / HISTORIALES
# ---------------------------------------------------
def get_current_patient():
    global CURRENT_PATIENT
    return CURRENT_PATIENT or "Paciente sin nombre"


def set_current_patient(name):
    global CURRENT_PATIENT
    if not name.strip():
        name = "Paciente sin nombre"
    CURRENT_PATIENT = name
    if name not in PATIENT_HISTORY:
        PATIENT_HISTORY[name] = []


def compute_train_stats(history):
    train_attempts = sum(1 for h in history if h["mode"] == "train")
    train_success = sum(1 for h in history
                        if h["mode"] == "train" and h.get("match_target"))
    return train_attempts, train_success

def build_chart_data(history):
    """
    Construye datos para los reportes:
    para cada gesto, calcula la precisión acumulada (train) por intento.

    Devuelve una lista:
    [
      {
        "idx": 0,
        "name": "Open bottle (tripod grasp)",
        "models": [
          {
            "name": "CNN mejorada – Ventanas crudas (200×10, capa latente 64-D)",
            "values": [100.0, 90.0, 80.0, ...]  # precisión acumulada
          }
        ]
      },
      ...
    ]
    """
    chart = []

    for g_idx, g_name in GESTURE_LABELS.items():
        # Solo intentos de ENTRENAMIENTO de ese gesto
        attempts = [
            h for h in history
            if h.get("mode") == "train"
            and h.get("true_gesture_idx") == g_idx
        ]

        # history ya está en orden cronológico por append, así que no hace
        # falta ordenar. Si quisieras, podrías ordenar por timestamp.

        running_correct = 0
        total = 0
        values = []

        for h in attempts:
            total += 1
            if h.get("match_target"):
                running_correct += 1

            acc = 100.0 * running_correct / total
            values.append(round(acc, 1))

        # Como por ahora solo usas la CNN mejorada, armamos un único "modelo"
        model_series = []
        if values:
            # Tomamos el display name del primer intento, si existe
            model_name = attempts[0].get(
                "model_display",
                "CNN mejorada – Ventanas crudas (400×10, capa latente 64-D)"
            )
            model_series.append({
                "name": model_name,
                "values": values
            })

        chart.append({
            "idx": g_idx,
            "name": g_name,
            "models": model_series
        })

    return chart


# ---------------------------------------------------
# FILTROS (MISMOS QUE TU DATASET REAL)
# ---------------------------------------------------
def bandpass(signal, low=20, high=450, fs=FS, order=4):
    nyq = fs / 2
    b, a = butter(order, [low/nyq, high/nyq], btype="band")
    return filtfilt(b, a, signal, axis=0)


def notch(signal, fs=FS, freq=50, Q=30):
    b, a = iirnotch(freq/(fs/2), Q)
    return filtfilt(b, a, signal, axis=0)


def normalize(signal):
    mean = np.mean(signal, axis=0)
    std = np.std(signal, axis=0) + 1e-8
    return (signal - mean) / std


# ---------------------------------------------------
# CREAR VENTANAS (MISMA LÓGICA QUE USASTE)
# ---------------------------------------------------
def create_windows(signal, window_size=WINDOW_SIZE, overlap=OVERLAP):
    step = int(window_size * (1 - overlap))
    windows = []
    for i in range(0, len(signal) - window_size + 1, step):
        windows.append(signal[i:i+window_size])
    return np.array(windows)


# ---------------------------------------------------
# PROCESAMIENTO FINAL DE EMG
# ---------------------------------------------------
def process_emg(raw_emg):
    """
    raw_emg: numpy array (N_samples, 10 canales)
    Devuelve: (1, 400, 10)  # una ventana de 400 muestras × 10 canales
    """

    emg = notch(raw_emg)
    emg = bandpass(emg)
    emg = normalize(emg)

    windows = create_windows(emg, WINDOW_SIZE, OVERLAP)
    if len(windows) == 0:
        raise ValueError("La señal es demasiado corta.")

    win = windows[0]
    return win.reshape(1, WINDOW_SIZE, N_CHANNELS)


# ---------------------------------------------------
# PREDICCIÓN CON CNN REAL
# ---------------------------------------------------
def predict_cnn_mejorada(raw_emg):
    """raw_emg: numpy array (N_samples, 10 canales)"""
    global CNN_MODEL

    if CNN_MODEL is None:
        # fallback dummy si no se cargó el modelo
        probs = np.array([0.25, 0.25, 0.25, 0.25])
        return 0, probs.tolist()

    x = process_emg(raw_emg)                # (1, 200, 10)
    probs = CNN_MODEL.predict(x, verbose=0)[0]  # (4,)
    pred_idx = int(np.argmax(probs))
    return pred_idx, probs.tolist()

# ---------------------------------------------------
# GENERAR EMG SIMULADA (para demo)
# ---------------------------------------------------
def simulate_emg_raw_for_gesture(g_idx, n_samples=2000, n_channels=10):
    amp = [0.6, 0.8, 0.7, 0.9][g_idx]
    noise = np.random.randn(n_samples, n_channels) * 0.25
    pattern = np.sin(np.linspace(0, 10*np.pi, n_samples))[:, None] * amp
    return (noise + pattern * (np.random.rand(1, n_channels) + 0.5)).astype(np.float32)


# ---------------------------------------------------
# GRAFICADO
# ---------------------------------------------------
def prepare_emg_plot(raw_emg):
    ch0 = raw_emg[:, 0]
    win = 50
    rms = np.sqrt(np.convolve(ch0**2, np.ones(win)/win, mode="same"))
    ds = max(1, len(ch0)//800)
    return {
        "raw": ch0[::ds].tolist(),
        "rms": rms[::ds].tolist()
    }


# ---------------------------------------------------
# RUTAS
# ---------------------------------------------------
@app.route("/")
def home():
    return redirect(url_for("classify"))


# ---------------------------------------------------
# CLASIFICACIÓN
# ---------------------------------------------------
@app.route("/classify", methods=["GET", "POST"])
def classify():
    patient = get_current_patient()
    result = None
    emg_plot = None

    if request.method == "POST":

        # 1. Nombre de paciente
        patient_name = request.form.get("patient_name", "")
        set_current_patient(patient_name)
        patient = get_current_patient()
        history = PATIENT_HISTORY[patient]

        # 2. Cargar archivo .npy si existe
        file = request.files.get("emg_file")
        raw_emg = None

        if file and file.filename.endswith(".npy"):
            try:
                raw_emg = np.load(file.stream)
                raw_emg = np.array(raw_emg, dtype=np.float32)

                if raw_emg.ndim == 2 and raw_emg.shape[1] == 10:
                    pass
                elif raw_emg.ndim == 2 and raw_emg.shape[0] == 10:
                    raw_emg = raw_emg.T
                elif raw_emg.ndim == 2 and raw_emg.shape[1] > 10:
                    raw_emg = raw_emg[:, :10]
                else:
                    raise ValueError("Formato inválido: se requiere matriz Nx10.")

                print("📥 EMG real cargada:", raw_emg.shape)

            except Exception as e:
                print("⚠ Error cargando archivo .npy:", e)
                raw_emg = None

        # 3. Si NO hay .npy → usar simulada
        if raw_emg is None:
            true_gesture_idx = int(np.random.choice([0, 1, 2, 3]))
            raw_emg = simulate_emg_raw_for_gesture(true_gesture_idx)
            real_name = GESTURE_LABELS[true_gesture_idx]
        else:
            true_gesture_idx = None
            real_name = "(desconocido – archivo cargado)"

        # 4. Clasificación real
        pred_idx, probs = predict_cnn_mejorada(raw_emg)

        confidence_pct = round(max(probs) * 100, 1)
        if max(probs) >= 0.9:
            level = "high"
        elif max(probs) >= 0.7:
            level = "medium"
        else:
            level = "low"

        # Guardar histórico
        attempt = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "mode": "classify",
            "patient": patient,
            "model_name": "cnn_mejorada",
            "model_display": MODEL_DISPLAY["cnn_mejorada"],
            "true_gesture_idx": true_gesture_idx,
            "true_gesture_name": real_name,
            "gesture_idx": pred_idx,
            "gesture_name": GESTURE_LABELS[pred_idx],
            "confidence_pct": confidence_pct,
            "target_gesture": None,
            "match_target": None
        }
        history.append(attempt)

        emg_plot = prepare_emg_plot(raw_emg)

        train_attempts, train_success = compute_train_stats(history)

        result = {
            "patient": patient,
            "model_display": MODEL_DISPLAY["cnn_mejorada"],
            "true_gesture_name": real_name,
            "gesture_idx": pred_idx,
            "gesture_name": GESTURE_LABELS[pred_idx],
            "confidence_pct": confidence_pct,
            "confidence_level": level,
            "probs": [{"idx": i, "name": GESTURE_LABELS[i], "prob": round(probs[i]*100, 1)}
                      for i in range(4)],
            "train_attempts": train_attempts,
            "train_success": train_success
        }

    return render_template(
        "classify.html",
        active_page="classify",
        patient=patient,
        result=result,
        emg_plot=emg_plot,
        gesture_labels=GESTURE_LABELS
    )


# ---------------------------------------------------
# ENTRENAMIENTO GUIADO
# ---------------------------------------------------
@app.route("/train", methods=["GET", "POST"])
@app.route("/train", methods=["GET", "POST"])
def train():
    patient = get_current_patient()
    result = None

    if request.method == "POST":

        # 1. Nombre de paciente
        patient_name = request.form.get("patient_name", "")
        set_current_patient(patient_name)
        patient = get_current_patient()

        history = PATIENT_HISTORY[patient]

        # 2. Gesto objetivo (obligatorio en el form)
        target = int(request.form.get("target_gesture"))

        # 3. Intentar cargar archivo .npy (opcional)
        file = request.files.get("emg_file")
        raw_emg = None

        if file and file.filename.endswith(".npy"):
            try:
                raw_emg = np.load(file.stream)
                raw_emg = np.array(raw_emg, dtype=np.float32)

                if raw_emg.ndim == 2 and raw_emg.shape[1] == 10:
                    pass
                elif raw_emg.ndim == 2 and raw_emg.shape[0] == 10:
                    raw_emg = raw_emg.T
                elif raw_emg.ndim == 2 and raw_emg.shape[1] > 10:
                    raw_emg = raw_emg[:, :10]
                else:
                    raise ValueError("Formato inválido: se requiere matriz Nx10.")

                print("📥 EMG real cargada en /train:", raw_emg.shape)

            except Exception as e:
                print("⚠ Error cargando archivo .npy en /train:", e)
                raw_emg = None

        # 4. Si NO hay archivo válido → seguimos usando EMG simulada como fallback
        if raw_emg is None:
            raw_emg = simulate_emg_raw_for_gesture(target)

        # 5. Clasificación con la CNN
        pred_idx, probs = predict_cnn_mejorada(raw_emg)

        confidence_pct = round(max(probs) * 100, 1)
        level = "high" if max(probs) >= 0.9 else ("medium" if max(probs) >= 0.7 else "low")
        match = (pred_idx == target)

        feedback = (
            "✅ Acierto. Mantén el gesto 2–3 s y repite varias veces."
            if match else
            "❌ No coincide. Ajusta la postura de dedos y antebrazo."
        )

        # 6. Guardar histórico
        attempt = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "mode": "train",
            "patient": patient,
            "model_name": "cnn_mejorada",
            "model_display": MODEL_DISPLAY["cnn_mejorada"],
            "true_gesture_idx": target,
            "true_gesture_name": GESTURE_LABELS[target],
            "gesture_idx": pred_idx,
            "gesture_name": GESTURE_LABELS[pred_idx],
            "confidence_pct": confidence_pct,
            "target_gesture": target,
            "match_target": match
        }
        history.append(attempt)

        train_attempts, train_success = compute_train_stats(history)

        result = {
            "patient": patient,
            "target_gesture_idx": target,
            "target_gesture_name": GESTURE_LABELS[target],
            "gesture_idx": pred_idx,
            "gesture_name": GESTURE_LABELS[pred_idx],
            "confidence_pct": confidence_pct,
            "confidence_level": level,
            "feedback_text": feedback,
            "session_attempts": train_attempts,
            "session_success": train_success,
            "session_success_pct": round(
                (train_success/train_attempts*100) if train_attempts > 0 else 0, 1
            )
        }

    return render_template(
        "train.html",
        active_page="train",
        gesture_labels=GESTURE_LABELS,
        patient=patient,
        result=result
    )

# ---------------------------------------------------
# REPORTES
# ---------------------------------------------------
@app.route("/reports")
def reports():
    patient = get_current_patient()
    history = PATIENT_HISTORY.get(patient, [])
    train_attempts, train_success = compute_train_stats(history)

    stats = {
        "total_attempts": len(history),
        "train_attempts": train_attempts,
        "train_success": train_success,
        "train_success_pct": round(
            (train_success/train_attempts*100) if train_attempts > 0 else 0, 1
        )
    }

    # 👉 construir datos para las gráficas
    chart_data = build_chart_data(history)

    return render_template(
        "reports.html",
        active_page="reports",
        patient=patient,
        history=history,
        stats=stats,
        gesture_labels=GESTURE_LABELS,
        chart_data=chart_data    # <<< clave
    )


# ---------------------------------------------------
# ABOUT
# ---------------------------------------------------
@app.route("/about")
def about():
    patient = get_current_patient()
    return render_template(
        "about.html",
        active_page="about",
        patient=patient
    )


# ---------------------------------------------------
# PDF EXPORT
# ---------------------------------------------------
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

@app.route("/download_pdf")
@app.route("/download_pdf")
def download_pdf():
    patient = get_current_patient()
    history = PATIENT_HISTORY.get(patient, [])
    train_attempts, train_success = compute_train_stats(history)

    # --- Métricas globales ---
    if train_attempts > 0:
        train_accuracy = round(train_success / train_attempts * 100, 1)
    else:
        train_accuracy = None

    # Accuracy por gesto (solo modo train)
    per_gesture_stats = []
    for g_idx, g_name in GESTURE_LABELS.items():
        attempts_g = [
            h for h in history
            if h.get("mode") == "train" and h.get("true_gesture_idx") == g_idx
        ]
        total_g = len(attempts_g)
        success_g = sum(1 for h in attempts_g if h.get("match_target"))
        acc_g = round(success_g / total_g * 100, 1) if total_g > 0 else None
        per_gesture_stats.append({
            "idx": g_idx,
            "name": g_name,
            "total": total_g,
            "success": success_g,
            "acc": acc_g
        })

    # --- Preparar PDF ---
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    w, h = A4

    y = h - 50
    c.setFont("Helvetica-Bold", 14)
    c.drawString(40, y, f"Reporte EMG – Paciente: {patient}")
    y -= 25

    c.setFont("Helvetica", 10)
    c.drawString(40, y, f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    y -= 20

    # Resumen global
    c.drawString(40, y, f"Intentos totales: {len(history)}")
    y -= 14
    c.drawString(40, y, f"Intentos entrenamiento: {train_attempts}")
    y -= 14
    c.drawString(40, y, f"Aciertos entrenamiento: {train_success}")
    y -= 14
    if train_accuracy is not None:
        c.drawString(40, y, f"Accuracy global entrenamiento: {train_accuracy}%")
        y -= 20
    else:
        c.drawString(40, y, "Accuracy global entrenamiento: –")
        y -= 20

    # Tabla resumen por gesto
    c.setFont("Helvetica-Bold", 11)
    c.drawString(40, y, "Resumen por gesto:")
    y -= 16
    c.setFont("Helvetica", 9)

    c.drawString(40, y, "Gesto")
    c.drawString(220, y, "Intentos")
    c.drawString(290, y, "Aciertos")
    c.drawString(360, y, "Accuracy (%)")
    y -= 12

    for g in per_gesture_stats:
        if y < 80:
            c.showPage()
            y = h - 50
            c.setFont("Helvetica-Bold", 11)
            c.drawString(40, y, "Resumen por gesto (cont.):")
            y -= 16
            c.setFont("Helvetica", 9)

        acc_txt = f"{g['acc']}%" if g["acc"] is not None else "–"
        c.drawString(40, y, f"Clase {g['idx']} – {g['name']}")
        c.drawString(220, y, str(g["total"]))
        c.drawString(290, y, str(g["success"]))
        c.drawString(360, y, acc_txt)
        y -= 12

    y -= 18

    # --- Gráfico de precisión acumulada usando tu lógica de build_chart_data ---
    chart_data = build_chart_data(history)

    # Ver si hay algún gesto con datos
    hay_datos = any(g["models"] and g["models"][0]["values"] for g in chart_data)

    if hay_datos:
        # Crear figura con matplotlib
        fig, ax = plt.subplots(figsize=(6, 3))
        for g in chart_data:
            if not g["models"]:
                continue
            serie = g["models"][0]["values"]
            if not serie:
                continue
            x_vals = list(range(1, len(serie) + 1))
            ax.plot(x_vals, serie, marker="", linewidth=1, label=g["name"])

        ax.set_xlabel("Intento de entrenamiento")
        ax.set_ylabel("Precisión acumulada (%)")
        ax.set_title("Evolución de precisión por gesto")
        ax.set_ylim(0, 105)
        ax.legend(fontsize=6)
        fig.tight_layout()

        img_buffer = BytesIO()
        fig.savefig(img_buffer, format="PNG", dpi=150)
        plt.close(fig)
        img_buffer.seek(0)

        img = ImageReader(img_buffer)
        img_width = w - 80
        img_height = img_width * 0.45  # proporción aprox

        # Si no hay espacio, nueva página
        if y - img_height < 60:
            c.showPage()
            y = h - 60

        c.drawImage(img, 40, y - img_height, width=img_width, height=img_height)
        y = y - img_height - 20  # bajar el cursor bajo la imagen

    # --- Historial detallado (texto más ordenado) ---
    if y < 80:
        c.showPage()
        y = h - 50

    c.setFont("Helvetica-Bold", 11)
    c.drawString(40, y, "Historial detallado:")
    y -= 18
    c.setFont("Helvetica", 9)

    for hst in history:
        if y < 60:
            c.showPage()
            y = h - 50
            c.setFont("Helvetica-Bold", 11)
            c.drawString(40, y, "Historial detallado (cont.):")
            y -= 18
            c.setFont("Helvetica", 9)

        # Línea 1: fecha, modo, modelo
        line1 = (
            f"{hst['timestamp']} | Modo: {hst['mode']} | "
            f"Modelo: {hst.get('model_display', hst.get('model_name', ''))}"
        )
        c.drawString(40, y, line1)
        y -= 12

        # Línea 2: gesto detectado, confianza, objetivo y resultado (si aplica)
        line2 = (
            f"Gesto detectado: {hst['gesture_name']} | "
            f"Confianza: {hst['confidence_pct']}%"
        )

        if hst["mode"] == "train":
            tgt = GESTURE_LABELS[hst["target_gesture"]]
            resultado = "Acierto" if hst["match_target"] else "Fallo"
            line2 += f" | Objetivo: {tgt} | {resultado}"

        c.drawString(60, y, line2)
        y -= 14

    c.showPage()
    c.save()
    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name=f"Reporte_{patient.replace(' ', '_')}.pdf",
        mimetype="application/pdf"
    )


@app.route("/dashboard")
def dashboard():
    patient = get_current_patient()
    history = PATIENT_HISTORY.get(patient, [])

    # Siempre calculamos estas métricas, aunque sean 0
    train_attempts, train_success = compute_train_stats(history)

    if train_attempts > 0:
        train_accuracy = round(train_success / train_attempts * 100, 1)
    else:
        train_accuracy = None

    overview = {
        "total_attempts": len(history),
        "train_attempts": train_attempts,
        "train_success": train_success,
        "train_accuracy": train_accuracy
    }

    return render_template(
        "dashboard.html",
        active_page="dashboard",
        patient=patient,
        overview=overview
    )

# ---------------------------------------------------
# MAIN
# ---------------------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)