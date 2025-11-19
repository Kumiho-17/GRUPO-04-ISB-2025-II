# 🫀 Procesamiento de Señales ECG: Detección de Ondas P, QRS y T en una Señal SVTA

## 📑 Tabla de Contenidos

1. [Introducción](#1-introducción)

2. [Fundamentos Teóricos](#2-fundamentos-teóricos)  
   - 2.1. [Electrocardiograma (ECG)](#21-electrocardiograma-ecg)  
   - 2.2. [Morfología de la señal: ondas P, QRS y T](#22-morfología-de-la-señal-ondas-p-qrs-y-t)  
   - 2.3. [Taquicardia Supraventricular (SVTA)](#23-taquicardia-supraventricular-svta)

3. [Objetivos del Laboratorio](#3-objetivos-del-laboratorio)

4. [Materiales y Señal Utilizada](#4-materiales-y-señal-utilizada)

5. [Metodología](#5-metodología)  
   - 5.1. [Importación de librerías pertinentes](#51-importación-de-librerías-pertinentes)  
   - 5.2. [Carga del dataset y selección de la señal SVTA](#52-carga-del-dataset-y-selección-de-la-señal-svta)  
   - 5.2. [Visualización de la señal](#53-visualización-de-la-señal)  
   - 5.3. [Detección del complejo QRS](#54-detección-del-complejo-qrs)  
   - 5.4. [Detección de la onda P](#55-detección-de-la-onda-p)  
   - 5.5. [Detección de la onda T](#56-detección-de-la-onda-t)  
   - 5.6. [Zoom en un ciclo cardíaco](#57-zoom-en-un-ciclo-cardíaco)  
   - 5.7. [Cálculo de intervalos RR y frecuencia cardíaca](#58-cálculo-de-intervalos-rr-y-frecuencia-cardíaca)

6. [Resultados](#6-resultados)  
   - 6.1. [Detección individual de cada onda](#61-detección-individual-de-cada-onda)  
   - 6.2. [Señal completa con ondas P-QRS-T marcadas](#62-señal-completa-con-ondas-p-qrs-t-marcadas)  
   - 6.3. [Frecuencia cardíaca instantánea (HR)](#63-frecuencia-cardíaca-instantánea-hr)

7. [Discusión](#7-discusión)

8. [Conclusiones](#8-conclusiones)

9. [Referencias](#9-referencias)

10. [Participación](#10-participación)


# 1. Introducción

El electrocardiograma (ECG) es una de las herramientas más utilizadas para evaluar la actividad eléctrica del corazón, ya que permite identificar la despolarización auricular (onda P), la despolarización ventricular (complejo QRS) y la repolarización ventricular (onda T). Estas ondas representan transiciones entre configuraciones eléctricas estables del miocardio, y su análisis detallado es fundamental para comprender el estado funcional del sistema de conducción cardíaco [1]. Debido a su gran utilidad bridando información relevante, el ECG continúa siendo un método indispensable tanto en investigación fisiológica como en la práctica clínica, pese al crecimiento de técnicas más modernas [2].

En este laboratorio se trabaja con una señal real perteneciente a la categoría SVTA (Taquicardia Supraventricular), una arritmia caracterizada por actividad eléctrica rápida originada por encima de los ventrículos. La SVTA suele presentar frecuencias cardíacas elevadas, variación en la relación P–QRS y, en muchos casos, ondas P atípicas o superpuestas al QRS, lo que dificulta su identificación visual [3]. El análisis por computadora permite mejorar la delimitación mediante técnicas avanzadas de procesamiento (filtrado, detección automática de picos y algoritmos especializados para ondas P y T).

El objetivo del laboratorio realizado es detectar y visualizar las ondas P, QRS y T de una señal ECG real mediante el uso de métodos automatizados  mediante herramientas como *neurokit2* y algoritmos establecidos para la identificación de complejos cardíacos. La combinación de estas técnicas facilita la interpretación de un las sñales EEG, y particularmente para este laboratorio facilita la interpretación de ritmo supraventricular acelerado, permitiendo observar alteraciones típicas como intervalos RR acortados y variabilidad dinámica en la frecuencia cardíaca.

# 2. Fundamentos Teóricos

## 2.1. Electrocardiograma (ECG)

El electrocardiograma registra las variaciones del campo eléctrico cardíaco generadas durante cada ciclo cardíaco. Estas variaciones reflejan la actividad del sistema de conducción: despolarización de aurículas, despolarización de ventrículos y repolarización ventricular. Desde la biosfica, el ECG puede interpretarse como una serie de transiciones entre configuraciones eléctricas relativamente estables en el tejido cardiaco, cuyo análisis permite inferir el estado de la conducción eléctrica y la función cardíaca global [1]. Gracias a su accesibilidad y alto valor diagnóstico, el ECG continúa vigente como herramienta clínica estándar incluso frente a metodologías más complejas [2].

## 2.2. Morfología de la señal: ondas P, QRS y T

La señal ECG normal se compone de tres elementos principales:  
- Onda P: representa la despolarización auricular.  
- Complejo QRS:refleja la despolarización ventricular y es el componente de mayor amplitud y pendiente.  
- Onda T: corresponde a la repolarización ventricular y presenta una morfología más suave y ancha que el QRS.

Cada una de estas ondas posee características distintivas en amplitud, duración y posición temporal dentro del ciclo cardíaco. El analisis conjunto de estas ondas permite evaluar el origen del ritmo, la relación auriculo-ventricular y la presencia de anomalías en la conducción o en la repolarización [1,4]. Asmimso, en situaciones patológicas, estas morfologías pueden alterarse, superponerse o deformarse, lo que complica su analisis de forma manual.

## 2.3. Taquicardia Supraventricular (SVTA)

La taquicardia supraventricular (SVTA) agrupa un conjunto de ritmos rápidos cuya actividad eléctrica se origina por encima de los ventrículos, ya sea en el nodo auriculo-ventricular, las aurículas o vías accesorias. La SVTA se caracteriza por frecuencias cardíacas elevadas (comúnmente entre 140 y 250 bpm), intervalos RR cortos y, en algunos casos, ondas P ocultas o invertidas dependiendo del mecanismo de reentrada o foco ectópico involucrado [3]. Estas alteraciones generan conducción irregular, variabilidad en la morfología del complejo  QRS o cambios en la relación temporal entre la onda P y el complejo QRS, lo que presenta un reto en el diagnóstico cuando se analizan señales ruidosas o de corta duración.

# 3. Objetivos

## 3.1. Objetivo general
Detectar y analizar las ondas P, QRS y T en una señal electrocardiográfica real de la clase SVTA, empleando técnicas de procesamiento digital y algoritmos automatizados basados en *neurokit2* para la delimitación morfológica del ciclo cardíaco.

## 3.2. Objetivos específicos
- Cargar, visualizar y describir la señal ECG seleccionada del dataset ECG.
- Implementar la detección automática de picos R (complejo QRS) como referencia para el análisis del ciclo cardíaco.
- Identificar las ondas P y T mediante algoritmos modernos de filtrado, realce y segmentación del ECG.
- Graficar de forma individual y conjunta las ondas P–QRS–T en la señal SVTA.
- Calcular y analizar los intervalos RR y la frecuencia cardíaca instantánea (HR) para caracterizar la dinámica del ritmo supraventricular.
- Interpretar los patrones observados en función de las características típicas de la taquicardia supraventricular.

# 4. Materiales y Señal Utilizada

Para el desarrollo del presente laboratorio se emplearon herramientas de software y un conjunto de datos con fragmentos reales de ECG. A continuación se detallan los elementos utilizados:

## 4.1. Materiales de software

| **Material / Software** | **Imagen** |
|--------------------------|------------|
| Python 3.12              | *(pendiente)* |
| Jupyter Notebook         | *(pendiente)* |
| neurokit2                | *(pendiente)* |
| numpy                    | *(pendiente)* |
| scipy                    | *(pendiente)* |
| matplotlib               | *(pendiente)* |
| pickle                   | *(pendiente)* |
| tqdm                     | *(pendiente)* |


## 4.2. Dataset empleado

Se utilizó el dataset ECG signals, disponible en Mendeley Data, el cual contiene registros de señales electrocardiográficas categorizadas en diferentes tipos de ritmos cardíacos. Cada archivo corresponde a un fragmento de señal en formato digital, previamente muestreado y etiquetado.

- **Fuente del dataset:**  
  Mendeley Data, DOI: https://doi.org/10.17632/7dybx7wyfn.3  

- **Archivo utilizado:**  
  `dataset_ekg.pkl` (proporcionado por el docente)

- **Frecuencia de muestreo:**  
  `fs = 360 Hz` (valor estándar en registros MIT-BIH)

## 4.3. Señal seleccionada

Para el análisis se seleccionó una señal correspondiente a la clase **SVTA** (Supraventricular Tachycardia), caracterizada por una frecuencia cardíaca rápida de origen supraventricular. La selección se realizó en base al índice:

- **Clase:** `SVTA`  
- **Fila:** `0`  
- **Duración:** igual al fragmento digital cargado  
- **Muestreo:** 360 Hz  

Esta señal se procesó a fin de identificar de manera automática las ondas P, QRS y T, además de realizar un análisis adicional mediante el cálculo de intervalos RR y frecuencia cardíaca instantánea.

# 5. Metodología

Dado que la señal ECG utilizada proviene de un dataset previamente adquirido y procesado, la metodología de este laboratorio se centró exclusivamente en el procesamiento digital de la señal y en la detección automática de sus componentes morfológicos. A continuación, se detalla el flujo de trabajo completo seguido en el análisis.

## 5.1. Importación de librerías pertinentes

Para el procesamiento se importaron las siguientes bibliotecas:

- `numpy` para manejo de arreglos y operaciones numéricas.  
- `matplotlib` para la visualización y graficación de la señal.  
- `scipy.signal` para operaciones de filtrado y manejo de señales.  
- `neurokit2` para la detección automática de ondas P, QRS y T.  
- `pickle` para la carga del dataset en formato `.pkl`.  
- `tqdm` para control de procesos iterativos.  

Estas librerías constituyen el conjunto básico para análisis en ingeniería biomédica durante prácticas de procesamiento de señales.

## 5.2. Carga de la señal y parámetros de muestreo

La señal seleccionada (clase SVTA, fila 0) fue cargada desde el archivo `dataset_ekg.pkl` mediante la librería `pickle`.  
Se confirmó una frecuencia de muestreo de 360 Hz, correspondiente al estándar utilizado en bases de datos como MIT-BIH.

Se generó el vector de tiempo asociado y se preparó la señal para su análisis posterior.

## 5.3. Visualización inicial del ECG

Se graficó la señal cruda en el dominio del tiempo utilizando `matplotlib`, con el fin de observar sus características morfológicas generales.  
En esta etapa se identificaron visualmente patrones consistentes con taquicardia supraventricular: intervalos RR acortados y complejos QRS relativamente estrechos.

## 5.4. Detección del complejo QRS

La identificación de los picos R se realizó mediante la función `ecg_process()` de *neurokit2*, la cual integra:

- filtrado en banda,  
- análisis de pendiente,  
- detección de energía,  
- umbrales adaptativos,  
- corrección del período refractario.

## 5.5. Detección de la onda P

La onda P fue detectada usando también las herramientas de delineación de neurokit2, que incorporan:

- filtrado en banda baja (0.5–15 Hz),  
- ventanas basadas en tiempos fisiológicos previos al QRS,  
- análisis de morfología local.  

## 5.6. Detección de la onda T

Los picos de la onda T fueron identificados utilizando los algoritmos internos de neurokit2, que analizan la región posterior al complejo QRS y detectan el máximo asociado a la repolarización ventricular.  
Previo a la graficación se eliminaron valores no válidos (NaN) para evitar errores de indexación.

## 5.7. Zoom en un ciclo cardíaco

Para una caracterización más precisa de la morfología, se seleccionó una ventana temporal donde ocurre un ciclo cardíaco completo.  
En este segmento se visualizaron y compararon las ondas P, QRS y T de manera aislada.

## 5.8. Cálculo de intervalos RR y frecuencia cardíaca

Utilizando los índices de picos R detectados, se calcularon:

- los intervalos RR en milisegundos,  
- la frecuencia cardíaca instantánea (HR)en bpm.

# 6. Resultados  

## 6.1. Visualización inicial de la señal ECG

![Señal ECG correspondiente a un episodio de SVTA]([images/ecg_signal.png](https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%2011/Imagenes/Figura1.png))

**Figura 1. Señal ECG correspondiente a un episodio de SVTA (fila 0)**  

En la Figura 1 se observa el fragmento de señal ECG seleccionado del dataset, clasificado como un episodio de taquicardia supraventricular (SVTA). La señal presenta una morfología característica, con complejos QRS estrechos y de alta amplitud distribuidos a intervalos regulares pero acortados.

La actividad eléctrica de base muestra oscilaciones de menor amplitud correspondientes a la actividad auricular, aunque la onda P no es claramente distinguible en todos los ciclos debido a la elevada frecuencia y posible solapamiento con el complejo QRS. Visualmente, se aprecia una repetición rápida de complejos ventriculares que sugiere un mecanismo de conducción acelerado, consistente con la fisiopatología del SVTA.

Este gráfico permite identificar preliminarmente el patrón rítmico general del episodio y sirve como punto de partida para la detección automática de las ondas P, QRS y T en secciones posteriores del análisis.

## 6.2. Detección del complejo QRS (picos R)

**Figura 2. Detección automática de los picos R del complejo QRS en la señal SVTA (fila 0)**  

En la Figura 2 se presenta el resultado del algoritmo de delineación aplicado a la señal ECG, donde los picos R han sido identificados y marcados con puntos rojos. Se observa una detección consistente a lo largo de todo el fragmento, lo cual confirma que el algoritmo reconoce adecuadamente los complejos QRS incluso bajo las condiciones de frecuencia elevada presentes en la taquicardia supraventricular.

Los complejos QRS detectados muestran una morfología estrecha y amplitud elevada, patrón compatible con arritmias supraventriculares en las que el origen del impulso eléctrico se encuentra por encima del nodo auriculoventricular. Asimismo, la distancia reducida entre picos R consecutivos refleja intervalos RR acortados.

Este resultado constituye la base para el cálculo de los intervalos RR y la frecuencia cardíaca instantánea, y sirve además como referencia temporal para la identificación posterior de las ondas P y T.

## 6.3. Detección de la onda P

**Figura 3. Detección automática de ondas P en la señal ECG — SVTA (fila 0)**  

En la Figura 3 se muestran las ondas P detectadas a lo largo del registro, marcadas con triángulos amarillos. Estas detecciones corresponden a la despolarización auricular y se observan principalmente en la porción basal de la señal, por delante del complejo QRS. Debido a la elevada frecuencia cardíaca característica de la taquicardia supraventricular, la onda P presenta amplitud reducida y en algunos ciclos se encuentra parcialmente superpuesta o cercana al complejo QRS, lo que dificulta su identificación visual.

A pesar de estas limitaciones fisiológicas y morfológicas, el algoritmo empleado logra localizar un número consistente de ondas P mediante análisis en banda baja y reconocimiento de patrones pre-QRS. 

La correcta detección de la onda P es especialmente relevante en episodios de SVTA, ya que permite distinguir entre distintos mecanismos de taquicardia y facilita la interpretación del origen supraventricular del ritmo.

## 6.4. Detección de la onda T

**Figura 4. Detección automática de ondas T en la señal ECG — SVTA (fila 0)**  

En la Figura 4 se presentan las ondas T identificadas por el algoritmo de delineación, marcadas con cuadrados verdes. Estas detecciones corresponden al proceso de repolarización ventricular y, como es habitual, aparecen después del complejo QRS. La morfología observada muestra ondas T de amplitud moderada y formas relativamente uniformes a lo largo del registro, lo que refleja una repolarización ventricular conservada.

A diferencia de la onda P, cuyo reconocimiento puede dificultarse por la cercanía temporal al QRS, la onda T mantiene una ventana fisiológica suficientemente amplia para permitir una detección más estable. No obstante, la frecuencia cardíaca elevada propia del SVTA ocasiona que las ondas T se encuentren más próximas entre sí, reduciendo el intervalo QT aparente y aumentando la superposición entre ciclos consecutivos.

La correcta identificación de la onda T es esencial para analizar la dinámica de la repolarización ventricular y para completar la delineación P–QRS–T del ciclo cardíaco, permitiendo un análisis integral de la actividad eléctrica durante el episodio de taquicardia.


## 6.5. Detección conjunta de ondas P, QRS y T

**Figura 5. Detección simultánea de ondas P, QRS (picos R) y T en la señal SVTA (fila 0)**  

En la Figura 5 se presenta la delineación completa del ciclo cardíaco, mostrando simultáneamente los tres componentes principales del ECG: la onda P (triángulos amarillos), el complejo QRS (picos R en rojo) y la onda T (cuadrados verdes). Esta visualización integrada permite apreciar la secuencia fisiológica completa de despolarización auricular, despolarización ventricular y repolarización ventricular a lo largo del registro.

La distribución temporal de las detecciones evidencia intervalos RR acortados, consistentes con la frecuencia elevada típica de la taquicardia supraventricular. A pesar de esta aceleración del ritmo, la delineación automática logra identificar correctamente la mayoría de las ondas P y T, incluso en los momentos en que su morfología presenta amplitudes reducidas o proximidad al complejo QRS.

Esta representación conjunta sintetiza el comportamiento eléctrico del corazón durante el episodio de SVTA, proporcionando una visión clara del patrón rítmico y facilitando el análisis posterior de intervalos, dinámicas de activación y variabilidad cardíaca.

## 6.6. Zoom en un ciclo cardíaco

**Figura 6. Zoom en un latido mostrando ondas P, QRS y T — SVTA (fila 0)**  

La Figura 6 muestra un acercamiento a un ciclo cardíaco completo con el fin de analizar en detalle la morfología de las ondas P, QRS y T. Este zoom permite identificar con mayor claridad la secuencia de activación auricular y ventricular, así como evaluar la precisión de la detección automática realizada por los algoritmos.

En el intervalo alrededor de 2.55 segundos se evidencia un solapamiento parcial entre la onda P y el final de la onda T. Esta superposición es una característica frecuente en episodios de taquicardia supraventricular, donde la elevada frecuencia cardíaca reduce el intervalo TP y puede hacer que la actividad auricular aparezca muy próxima —o incluso fusionada— con la despolarización ventricular.

Se observa que:
- La onda P presenta una amplitud baja y duración corta.  
- El complejo QRS es estrecho, alto y ocurre rápidamente después de la P.  
- La onda T aparece de manera clara tras el QRS, a pesar de la cercanía entre ciclos.  

Este análisis detallado confirma la correcta delineación P–QRS–T y resalta la fisiología acelerada característica del ritmo SVTA.

## 6.7. Frecuencia cardíaca instantánea (HR)

**Figura 7. Frecuencia cardíaca instantánea calculada a partir de los intervalos RR — SVTA (fila 0)**  

La Figura 7 muestra la frecuencia cardíaca instantánea obtenida a partir de los intervalos RR detectados en la señal ECG. Los valores iniciales se encuentran notablemente elevados, con picos entre 150 y 162 bpm, lo cual es característico de la taquicardia supraventricular, cuyo rango típico puede superar los 140 bpm según lo reportado en la literatura [3].

Los intervalos RR correspondientes reflejan esta aceleración del ritmo, con valores que comienzan alrededor de 370–420 ms, consistentes con una frecuencia auriculoventricular rápida. Conforme avanza el registro, se observa una variabilidad apreciable, con intervalos que aumentan hasta 800 ms y descienden nuevamente, lo cual genera oscilaciones de HR entre 73 y 126 bpm. Esta variabilidad puede deberse a fluctuaciones en la conducción AV o a la dinámica propia de la SVTA, en la cual la relación entre actividad auricular y ventricular puede modificarse de ciclo a ciclo.

La figura permite visualizar la transición desde un periodo de taquicardia marcada hacia intervalos de frecuencia más moderada, lo cual concuerda con la fisiología descrita en episodios de SVT, donde pueden coexistir fases de aceleración y desaceleración parcial del ritmo [3]. Este análisis cuantitativo complementa la inspección morfológica previa y aporta una visión temporal de la dinámica del ritmo supraventricular.

# 7. Discusión

Los resultados obtenidos permiten caracterizar la actividad eléctrica de un episodio de taquicardia supraventricular (SVTA). La morfología global de la señal, complejos QRS estrechos, intervalos RR acortados y ondas P de baja amplitud, son verificados a travez de la literatura para ritmos supraventriculares rápidos [3]. Este tipo de taquicardia se caracteriza por un mecanismo de activación auricular acelerado y conducción a través del nodo AV, lo que produce frecuencias cardíacas elevadas y un patrón rítmico distintivo. La señal analizada refleja estas características, confirmando su coherencia fisiológica.

En cuanto a la delineación del ECG, el algoritmo empleado logró identificar de manera consistente las ondas P, QRS y T incluso en condiciones de alta frecuencia cardíaca. La detección de picos R es fundamental para el análisis del ciclo cardíaco, y la literatura subraya que los algoritmos modernos presentan un desempeño coprecto y replicable en la identificación del complejo QRS, incluso en señales ruidosas y con complejas morfologias [5]. Además, la onda T fue detectada adecuadamente, lo que concuerda con los reportes sobre la importancia del análisis de la repolarización ventricular mediante técnicas automáticas de procesamiento [5].

Un hallazgo relevante se observa en el análisis con zoom del ciclo cardíaco, donde la onda T del ciclo previo, de baja amplitud, aparece muy próxima a la onda P del ciclo siguiente, generando un aparente solapamiento alrededor de 2.55 s. Este comportamiento coincide con lo dicho de ritmos supraventriculares rápidos, donde la reducción extrema del intervalo RR hace que la repolarización ventricular y la siguiente activación auricular ocurran con muy poca separación [3]. Además, estudios avanzados sobre detección de la onda P han demostrado que esta puede volverse menos visible o confundirse con la onda T en patologías y condiciones de alta frecuencia [4].

La frecuencia cardíaca instantánea mostró valores iniciales entre 150 y 160 bpm, seguidos de una disminución progresiva y oscilaciones marcadas entre ciclos. Esta variabilidad concuerda con lo reportado en episodios de SVTA, donde pueden presentarse fluctuaciones en la relación auriculoventricular y en la estabilidad del ritmo supraventricular [3].

# 8. Conclusiones

- Se logró delinear con éxito las ondas P, QRS y T en una señal ECG correspondiente a un episodio de taquicardia supraventricular (SVTA), confirmando la utilidad de los métodos automáticos de neurokit2 para el análisis del ciclo cardíaco.

- La señal presentó intervalos RR acortados, QRS estrechos y ondas P de baja amplitud, características típicas de los ritmos supraventriculares rápidos descritos en la literatura.

- El análisis con zoom permitió identificar un solapamiento entre la onda T y la onda P debido a la elevada frecuencia cardíaca, fenómeno fisiológicamente coherente con la dinámica de la SVTA.

- La frecuencia cardíaca instantánea mostró un inicio marcado de taquicardia seguido de variabilidad significativa entre ciclos, lo cual evidencia la naturaleza dinámica del episodio y refuerza la importancia del análisis combinado morfológico y temporal.

# 9. Referencias

[1] S. Kurbel, “A vector-free ECG interpretation with P, QRS & T waves as unbalanced transitions between stable configurations of the heart electric field,” *Theoretical Biology and Medical Modelling*, vol. 11, no. 10, pp. 1–14, 2014.

[2] T. Stracina, M. Ronzhina, R. Redina, and M. Novakova, “Golden Standard or Obsolete Method? Review of ECG Applications in Clinical and Experimental Context,” *Frontiers in Physiology*, vol. 13, Apr. 2022.

[3] I. D. Kotadia, S. E. Williams, and M. O’Neill, “Supraventricular tachycardia: An overview of diagnosis and management,” *Clinical Medicine*, vol. 20, no. 1, pp. 43–47, Jan. 2020.

[4] L. Maršánová, A. Němcová, R. Smíšek, M. Vítek, and L. Smital, “Advanced P wave detection in ECG signals during pathology: Evaluation in different arrhythmia contexts,” *Scientific Reports*, vol. 9, Dec. 2019.

[5] H. Ponnam and J. Hussain, “A comprehensive review on accurate QRS and T wave detection techniques for confirming cardiac abnormalities,” in *Proc. ICRAEC*, 2019, pp. 1–6.

# 10. Participación

| Integrante         | Porcentaje de participación |
|--------------------|-----------------------------|
| Eduardo Poma       | 33.33%                      |
| Rodrigo Gorbeña    | 33.33%                      |
| Jennifer Cancino   | 33.33%                      |

