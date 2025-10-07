## Transformada Wavelet
### :date:Tabla de contenidos

  - [1. Introducción](#page_facing_up1-introducción)
  - [2. Objetivos](#pushpin2-objetivos)
  - [3. Materiales](#pencil23-materiales)
  - [4. Metodología](#clipboard4-metodología)
    - [4.1. Diseño del filtro Wavelet para EMG](#41-diseño-del-filtro-wavelet-para-emg)
    - [4.2. Diseño del filtro Wavelet para ECG](#42-diseño-del-filtro-wavelet-para-ecg)
    - [4.3. Diseño del filtro Wavelet para EEG](#43-diseño-del-filtro-wavelet-para-eeg)
  - [5. Resultados](#chart_with_upwards_trend5-resultados)
    - [5.1. Señales EMG filtradas](#51-señales-emg-filtradas)
    - [5.2. Señales ECG filtradas](#52-señales-ecg-filtradas)
    - [5.3. Señales EEG filtradas](#53-señales-eeg-filtradas)
  - [6. Discusión](#bookmark_tabs6-discusión)
  - [Referencias](#notebookreferencias)
  - [Participación](#raised_handparticipación)
  
### :page_facing_up:1. Introducción
<p align="justify">
El electrocardiograma (ECG), electromiograma (EMG) y electroencefalograma (EEG), son herramientas fundamentales para el diagnóstico clínico e investigación biomédica ya que a través de su análisis se puede detectar alteraciones fisiológicas. Sin embargo, al mismo tiempo, estas señales son susceptibles a interferencias externas e internas que dificultan su interpretación.
<p align="justify">
El procesamiento de señales hace uso de herramientas como la Transformada de Fourier, que permite identificar los componentes frecuenciales de una señal. No obstante, esto ofrece solo una visión global del espectro, sin información sobre la localización temporal de los eventos, lo que limita el análisis de señales que cambian con el tiempo [1].
<p align="justify">
Frente a esto, la Transformada Wavelet es usada para el procesamiento de señales no estacionarias porque permite conservar la información temporal y frecuencial, adaptando resolución en función de escala: alta resolución temporal para frecuencias elevadas y alta resolución en frecuencia para frecuencias bajas [2]. Estas propiedades de la transformada sirven para detectar complejos QRS en ECG, artefactos de movimiento en EMG u ondas anómalas en EEG [3], [2], [4].
<p align="justify">
La Transformada Wavelet puede implementarse de dos formas. Transformada Wavelet Continua (CWT) que utiliza un rango continuo de escalas y posiciones, proporcionando precisión a costa de redundancia y costo computacional [5]. Transformada Wavelet Discreta (DWT) que emplea escalas y traslaciones discretas, eficiente para sistemas digitales. A parte de ello, tenemos la selección de la familia de wavelets, cuya elección influye en la calidad del análisis y fidelidad de la reconstrucción. Entre las más utilizadas tenemos a Haar, Daubechies, Symlets, Coiflets y Morlet [6].
<p align="justify">
En este contexto, este laboratorio presenta la implementación de filtros Wavelet. En particular, se analizaron y aplicaron los filtros a las señales EMG, ECG y EEG obtenidas de laboratorios previos, con el fin de evaluar su capacidad de mejora en la calidad de las señales.

### :pushpin:2. Objetivos
- **Objetivo general:**
  <p align="justify">
  Analizar y aplicar técnicas de procesamiento digital, enfocadas en EMG, ECG y EEG, mediante el diseño de filtros Wavelet, con el fin de mejorar la calidad de las señales y facilitar su interpretación.
</space>

- **Objetivos específicos:**
  - <p align="justify">Revisar y comparar las técnicas de diseño de filtros Wavelet.
  - <p align="justify">Implementar los filtros en señales EMG, ECG y EEG, para evaluar su desempeño en la reducción de ruido sin pérdida de información fisiológica relevante.
  - <p align="justify">Analizar los resultados de las señales EMG, ECG y EEG filtradas.

### :pencil2:3. Materiales
- **Hardware:**

    | Nombre | Cantidad | Descripción | Ilustración |
    |--------|----------|-------------|-------------|
    | **Laptop** | 1 | Computador portátil y compacto que integra pantalla, teclado y batería, sistema operativo de 64 bits. | ![image](https://intercompras.com/images/product/ACER_NH.Q2MAL.001.jpg) |
    
<center>Tabla 1: Hardware</center>

- **Software:**

    | Nombre | Descripción | Librerías | Ilustración |
    |--------|-------------|-----------|-------------|
    | **Python** | Lenguaje de programación con múltiples librerías en ciencia de datos y procesamiento de señales. | <ul><li>neurokit2</li><li>matplotlib</li><li>scipy</li><li>numpy</li></ul> | ![image](https://scratchpad.co.nz/wp-content/uploads/2020/07/learn-python-scaled.jpeg) |
<center>Tabla 2: Software [7]</center>

### :clipboard:4. Metodología
#### 4.1. Diseño del filtro Wavelet para EMG
<p align="justify">Para la señal EMG es importante resaltar que esta se encuentra usualmente entre los 20 a 500 Hz, pero la zona más útil para análisis se encuentra hasta los 150 o 200 Hz dependiendo de la naturaleza de la toma y además, esta señal oscila entre los 0 a 1.5 mVrms [7]. De esta manera esta señal se encuentra bastante vulnerable a anomalías provenientes de ruido, artefactos y otro tipo de interferencias, para lo cual es común realizar filtrados previos al análisis de la misma. En ese sentido, es bastante común el uso de la transformada Wavelet para filtrar la señal mediante su descomposición, pues en distintos estudios se a demostrado su eficacia para determinar y silenciar frecuencias no deseadas en comparación a otros métodos como filtros convencionales y FFT [8] catalogando resultados experimentales de DWT como superiores. Así pues, la DWT ha probado ser un cancelador de ruido para EMG proveniente de la inherencia del electrodo, ruido electromagnético, diafonías o ruido interno como se ha probado hasta en 5 funciones Wavelet (db2,db5,sym5, sym8 y coif5) para eliminar este ruido y tener una mejor señal para el control mioeléctrico multifunción [9]. Cabe resaltar que si bien se uso la familia coif5, esta ha presentado resultados algo extremos en análisis anteriores, por lo que se ha optado por trabajar con sus familias anteriores (coif1-coif4).

Es así que en la siguiente tabla se encuentran parámetros tomando en cuenta la familia coif4 siguiendo un análisis anterior realiza con la misma.

| Parámetros | Valor adoptado | Justificación |
|------------|----------------|---------------|
| **Familia** | coif4 | Presenta menor cantidad de errores en comparación a otras familias|
| **Orden** | 4 | Compromiso entre tiempo-frecuencia |
| **Nivel de descomposición (L)** | 4 | Balance entre eliminación de ruido y preservación |
| **Transformada** | DWT | Adecuada para filtrado discreto y reconstrucción |
| **Método de umbralado** | Soft threshold | Preserva morfología |
| **Regla del umbral** | Universal (VisuShrink) | Simple, dependiente del tamaño N |
| **Reconstrucción** | IDWT | Recupera señal filtrada sin pérdida |
| **Frecuencia de muestreo** | 1000 Hz | El rango de frecuencias de EMG es ligeramente grande |
<center>Tabla 3: Tabla de parametros para el filtro Wavelet en EMG</center>

#### 4.2. Diseño del filtro Wavelet para ECG
<p align="justify">Para el filtrado de la señal ECG se selecciona la familia Dubechies, específicamente en los órdenes db4-db6, debido a su alta similitud en morfología con el complejo QRS, además de su capacidad para representar eficazmente transiciones abruptas que son características de la actividad eléctrica cardiaca. Esta familia proporciona un adecuado balance entre la resolución temporal y frecuencial, lo que permite eliminar el ruido de alta y baja frecuencia sin distorsionar las ondas Py T. En algunos estudios se demostró que la función Daubechies 4 (db4) presenta una forma escalar semejante al ECG, logrando detectar picos R y otros componentes con una desviación inferior al 10% en MIT-BIH Arrhythmia Database [11]. Otro estudio confirma la eficacia de esta familia en ECG en adultos, en el que se evaluó Daubechies de orden 1 a 10 y concluyeron que los niveles de descomposición entre 3 y 5 maximizan la precisión (94 %) para detectar fibrilación auricular, mientras que db4 y db6 mantuvieron la morfología estable [12]. Además, se reporta que las familias Daubechies, Symlet y Coiflet ofrecen una mejor relación entre suavidad, soporte compacto y ortogonalidad para señales biomédicas no estacionarias en comparación de otras familias de wavelets con menor regularidad como Haar que presentan menor desempeño  [13]. Lo anteriormente descrito, respalda la elección de  como una adecuada alternativa para el filtrado ECG adulto para asegurar la preservación de rasgos clínicos esenciales de la señal.

| Parámetros | Valor adoptado | Justificación |
|------------|----------------|---------------|
| **Familia** | Daubechies (db4–db6) | Similar al complejo QRS, probado en MIT-BIH |
| **Orden** | 4 - 6 | Compromiso entre tiempo-frecuencia |
| **Nivel de descomposición (L)** | 4 | Balance entre eliminación de ruido y preservación |
| **Transformada** | DWT | Adecuada para filtrado discreto y reconstrucción |
| **Método de umbralado** | Soft threshold | Preserva morfología |
| **Regla del umbral** | Universal (VisuShrink) | Simple, dependiente del tamaño N |
| **Reconstrucción** | IDWT | Recupera señal filtrada sin pérdida |
| **Frecuencia de muestreo** | 1000 Hz | ECG adulto MIT-BIH |
<center>Tabla 4: Tabla de parametros para el filtro Wavelet en ECG</center>

#### 4.3. Diseño del filtro Wavelet para EEG
<p align="justify">Para filtrar señales EEG se optó por la familia Biorthogonal, en específico bior2.6, por su capacidad de suprimir ruido sin alterar la información del registro. Esta Wavelet presenta una reconstrucción precisa debido a sus pares de filtros de descomposición y reconstrucción, que permiten mantener la morfología de las ondas cerebrales aun tras la eliminación de ruido. Además, su estructura de soporte compacto proporciona un buen equilibrio entre resolución temporal y frecuencial. Estudios comparativos, evaluaron distintas familias (Symlet4, Haar, Daubechies4, Coiflets3, Discrete Meyer, Reverse Biorthogonal 6.8 y 2.8), y observaron que bior2.6 alcanzó los valores más altos de PSNR (≈46.7 dB para EEG epiléptico y 42.4 dB para EEG de sueño) y el menor MSE, superando a filtros como LMS y Butterworth [14].

| Parámetros | Valor adoptado | Justificación |
|------------|----------------|---------------|
| **Familia** | Biorthogonal | Más eficaz para eliminar el ruido en EEG |
| **Longitud de filtro** | Descomposición 2 - Reconstrucción 6 | Ofrece simetría, minimiza la distorsión de fase |
| **Nivel de descomposición (L)** | 5 | Permite equilibrar resolución temporal y frecuencial en señales no estacionarias |
| **Transformada** | DWT | Adecuada para filtrado discreto |
| **Coeficiente de aproximación** | A5 | Nos da la forma general de la señal |
| **Coeficientes de detalle** | D1, D2, D3, D4, D5 | Representan los cambios rápidos |
| **Reconstrucción** | IDWT | Recupera la señal manteniendo la forma de las ondas |
| **Frecuencia de muestreo** | 1000 Hz | EEG adulto |
<center>Tabla 5: Tabla de parametros para el filtro Wavelet en EEG</center>

### :chart_with_upwards_trend:5. Resultados
#### 5.1. Señales EMG filtradas
<p align="justify">La señal EMG fue filtrada mediante DWT con la familia Coiflet4 (nivel 4) y umbralado suave según se sigue en la literatura e investigaciones previamente realizadas. Así, se observaron los siguientes gráficos referidos a la señal cruda, filtrada y parámetros para la evaluación del filtro.  

<center><img src=https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%207%20-%20Wavelet/Images/EMG_1.png?raw=true/></center>
<center>Figura 1: Señal EMG original vs filtrada con coiflet 4. [Elaboración propia]</center>

<center><img src=https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%207%20-%20Wavelet/Images/EMG_r.png?raw=true/></center>
<center>Figura 2: Espectro antes vs despues del filtro. [Elaboración propia]</center>

<center><img src=https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%207%20-%20Wavelet/Images/EMG_e.png?raw=true/></center>
<center>Figura 3: Envolvente RMS para la señal filtrada. [Elaboración propia]</center>

<p align="justify">En las métricas, observadas se obtiene un filtrado relativamente efectivo en la figura 1, pues el cambio entre señal filtrada y no filtrada es ligero, sin embargo si es posible observar una mejora relativa en cuanto a atenuación lugares que parecen tener frecuencias más altas de lo debido. Así pues, esto se justifica mediante la figura 2, en la que se observa cómo el corte de frecuencias comienza aproximadamente por los 150 Hz al ver la atenuación entre la señal filtrada y no filtrada. Finalmente, en el caso de EMG, la gráfica envolvente de RMS permite determinar la efectividad del filtrado, por lo que mediante la figura 3 identificamos una RMS coherente con la señal filtrada durante el accionar de la señal que mediante literatura los valores cercanos a 0.75 y 1 permiten observar si el filtrado ha sido bueno.

#### 5.2. Señales ECG filtradas
<p align="justify">La señal ECG fue filtrada mediante DWT con Daubechies-6 (nivel 4) y umbralado suave (VisuShrink). La reconstrucción por IDWT preservó la morfología del complejo P–QRS–T, como se observa en la superposición original vs. filtrada (Fig. 4). La PSD de 0 a 100 Hz (Fig. 5) evidencia atenuación consistente de componentes de alta frecuencia (≥40 Hz), manteniendo la banda útil del ECG. El residual (Fig. 6) es de media cercana a cero, dominado por contenido rápido, lo que sugiere que el filtro removió principalmente ruido (EMG/alta frecuencia) y no algún componente fisiológico.

<center><img src=https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%207%20-%20Wavelet/Images/ECG_1.png?raw=true/></center>
<center>Figura 4: Señal ECG original vs filtrada con Daubechies-6. [Elaboración propia]</center>

<center><img src=https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%207%20-%20Wavelet/Images/ECG_e.png?raw=true/></center>
<center>Figura 5: Espectro antes vs despues del filtro. [Elaboración propia]</center>

<center><img src=https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%207%20-%20Wavelet/Images/ECG_r.png?raw=true/></center>
<center>Figura 6: Residual = Señal original - Filtrada. [Elaboración propia]</center>

<p align="justify">En las métricas, el filtrado incrementó la SNR de -8.23 dB a 28.87 dB, con una ganancia de +37.10dB lo que indica una gran reducción del ruido. La distorsión relativa fue baja (PDR = 3.59%) y el error cuadrático medio fue de RMSE = 8uV, que es coherente con una mínima alteración de la señal. La corrección entre la señal original y la filtrada fue de 0.999, esto confirma la alta fidelidad de la reconstrucción. En términos de preservación clinica, la frecuencia cardiaca permaneció inalterada (la diferencia ente HR antes y después del filtro fue de 0.0 bpm) y la amplitud pico-pico QRS objetivo tuvo una reducción de 0.98%, esto respalda el hecho que la morfología esencial se logró conservar. 

#### 5.3. Señales EEG filtradas
<p align="justify">La señal EEG fue filtrada mediante DWT con Biorthogonal (nivel 5). La reconstrucción por IDWT preservó la morfología general del trazado electroencefalográfico, como se observa en la superposición original vs. filtrada (Fig. 7). La PSD de 0 a 100 Hz (Fig. 8) evidencia atenuación consistente de componentes de alta frecuencia (≥80 Hz), manteniendo la banda útil del EEG. El residual (Fig. 9) es de media cercana a cero, lo que sugiere que el filtro removió principalmente ruido (parpadeos/EMG) y no algún componente fisiológico.

<center><img src=https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%207%20-%20Wavelet/Images/EEG_1.png?raw=true/></center>
<center>Figura 7: Señal ECG original vs filtrada con Biorthogonal. [Elaboración propia]</center>

<center><img src=https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%207%20-%20Wavelet/Images/EEG_e.png?raw=true/></center>
<center>Figura 8: Espectro antes vs despues del filtro. [Elaboración propia]</center>

<center><img src=https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%207%20-%20Wavelet/Images/EEG_r.png?raw=true/></center>
<center>Figura 9: Residual = Señal original - Filtrada. [Elaboración propia]</center>
  
<p align="justify">En las métricas, el filtrado incrementó la SNR de -3.62 dB a 18.23 dB, con una ganancia de +21.86 dB lo que indica una reducción del ruido. La distorsión relativa fue baja (PDR = 11.70%) y el error cuadrático medio fue de RMSE = 0.0205 mV, que es coherente con una mínima alteración de la señal. La corrección entre la señal original y la filtrada fue de 0.994, esto confirma la alta fidelidad de la reconstrucción.

### :bookmark_tabs:6. Discusión
- **Señales EMG**
  <p align="justify">Los resultados del filtrado DWT mediante la familia coiflet 4 revelan la efectividad del filtrado mediante la figura 2, así como la justificación de los parámetros usados, pues mediante el PSD obtenido se observa el funcionamiento del filtro al atenuar frecuencias más allá de 200 Hz que no corresponden a la zona útil de la señal EMG. Sin embargo dentro del espectro se observa un presunto pico en 60 Hz que puede corresponder al ruido eléctrico, por lo que si bien el filtro funciono bien para atenuar frecuencias superiores a las útiles, este no pudo arreglar el ruido proveniente de la red eléctrica, de tal manera que es necesario aplicar un filtro notch de 60 Hz para conseguir una mejor señal. En síntesis el filtro es efectivo para atenuar la mayoría de ruido fuera del rango de 20 Hz a 150 Hz pero si existe algún espectro dentro como 60 Hz por ejemplo, este presenta una debilidad al no poder atenuarlo.

- **Señales ECG**
  <p align="justify">Estos resultados respaldan y validan la elección de db6 y L=4, ya que se observa que el nivel de descomposición es suficiente para separar el ruido de alta frecuencia sin sobre-suavizar el QRS y el umbral suave evita discontinuidades en la reconstrucción y favorece la preservación de picos. Por otro lado, en la Figura 5 se aprecia un pico estrecho en torno a 60 Hz que está asociado a la interferencia de la red eléctrica. Dado que la DWT atenúa preferentemente ruido distribuido, este componente puede persistir. En caso que requiera una mayor supresión es posible combinar el filtrado wavelet con un filtro notch a 60 Hz. 

- **Señales EEG**
  <p align="justify">La aplicación de la familia Biorthogonal (bior2.6) y L = 5 elimino correctamente el ruido en la señal EEG, preservando la morfología y amplitud de las ondas cerebrales. Al superponer la señal original y filtrada, se observo que la reconstrucción mediante IDWT no generó distorsiones. El análisis espectral evidenció una atenuación consistente de componentes por encima de 30 Hz, asociadas principalmente a ruido EMG, mientras que las bandas fisiológicas (delta, theta, alfa y beta) se conservaron. Sin embargo, se mantuvo un pico en 60 Hz, causado por la interferencia de red eléctrica. Este podría suprimirse combinando el wavelet con regresión espectral (CleanLine), el cual elimina las componentes estacionarias asociadas a la red [15].

### :notebook:Referencias
<p align="justify">
1.	“Limitations of fourier analysis and need for wavelets | Signal Processing Class notes | Fiveable,” Fiveable. https://fiveable.me/fourier-analysis-wavelets-and-signal-processing/unit-9/limitations-fourier-analysis-wavelets/study-guide/093XH6BFqtUspkVa

<p align="justify">
2.	P. Zandiyeh, L. R. Parola, B. C. Fleming, and J. E. Beveridge, "Wavelet analysis reveals differential lower limb muscle activity patterns long after anterior cruciate ligament reconstruction," Journal of Biomechanics, vol. 133, p. 110957, 2022, doi: 10.1016/j.jbiomech.2022.110957.

<p align="justify">
3.	T. Sharma and K. K. Sharma, "QRS Complex Detection in ECG Signals Using the Synchrosqueezed Wavelet Transform," IETE Journal of Research, vol. 62, no. 6, pp. 885-892, Nov.-Dec. 2016, doi: 10.1080/03772063.2016.1221744.

<p align="justify">
4.	S. Mallat, "Chapter 3 - Discrete Revolution," in A Wavelet Tour of Signal Processing, 3rd ed., San Diego, CA, USA: Academic Press, 2009, pp. 59-88.

<p align="justify">
5.	R. González G., "Capítulo 3: Revisión de la Teoría de Wavelets," Universidad de las Américas Puebla, Puebla, México. Disponible: https://catarina.udlap.mx/u_dl_a/tales/documentos/mel/gonzalez_g_ra/capitulo3.pdf.

<p align="justify">
6.	E. Pinto Moreno, "Familias de Wavelets," Universidad Carlos III de Madrid, Madrid, España. Disponible: https://e-archivo.uc3m.es/bitstream/10016/16582/1/PFC_Elena_Pinto_Moreno_Anexos.pdf.

<p align="justify">
7. J. Kilby y H. Gholam Hosseini, “Wavelet analysis of surface electromyography signals,” en Proceedings of the IEEE Engineering in Medicine and Biology Society, 2004, pp. 384-387, doi:10.1109/IEMBS.2004.1403174.

<p align="justify">
8. Zhang, Y. Wang y R. Han, “Wavelet transform theory and its application in EMG signal processing,” en Proceedings of the 2010 Seventh International Conference on Fuzzy Systems and Knowledge Discovery (FSKD), vol. 5, pp. 5-6, 2010, doi:10.1109/FSKD.2010.5569532.

<p align="justify">
9. R. H. Chowdhury, M. B. I. Reaz, M. A. Ali, A. A. Bakar, K. Chellappan y T. G. Chang, “Surface electromyography signal processing and classification techniques,” Sensors, vol. 13, no. 9, pp. 12431–12466, 2013. doi:10.3390/s130912431.

<p align="justify">
10.	Welcome to [Internet]. Python.org. [citado el 20 de septiembre de 2025]. Disponible en: https://www.python.org/

<p align="justify">
11. M. A. Mohamed and M. Deriche, “An Approach for ECG Feature Extraction using Daubechies 4 (DB4) Wavelet,” International Journal of Computer Applications, vol. 96, no. 12, pp. 36–41, Jun. 2014, doi: 10.5120/16850-6712.

<p align="justify">
12. S. Mandala, A. R. P. Wibowo, Adiwijaya, Suyanto, M. S. M. Zahid, and A. Rizal, “The Effects of Daubechies Wavelet Basis Function (DWBF) and Decomposition Level on the Performance of Artificial Intelligence-Based Atrial Fibrillation (AF) Detection Based on Electrocardiogram (ECG) Signals,” Applied Sciences, vol. 13, no. 5, p. 3036, Feb. 2023, doi: 10.3390/app13053036.

<p align="justify">
13. C. Ouyang, L. Cai, B. Liu, and T. Zhang, “An Improved Wavelet Threshold Denoising Approach for Surface Electromyography Signal,” EURASIP Journal on Advances in Signal Processing, vol. 2023, no. 108, pp. 1–24, Oct. 2023, doi: 10.1186/s13634-023-01066-3.

<p align="justify">
14. “Comparative analysis of various filtering techniques for denoising EEG signals,” IEEE Conference Publication | IEEE Xplore, Apr. 02, 2021. https://ieeexplore.ieee.org/document/9417984

<p align="justify">
15. T. Mullen et al., “Real-time modeling and 3D visualization of source dynamics and connectivity using wearable EEG,” PubMed, pp. 2184–2187, Jul. 2013, doi: 10.1109/embc.2013.6609968.

### :raised_hand:Participación
- Eduardo Poma: 33.33%
- Rodrigo Gorbeña: 33.33%
- Jennifer Cancino: 33.33%