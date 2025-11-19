## Modelo autoregresivo - Yule Walker
### :date:Tabla de contenidos

  - [1. Introducción](#page_facing_up1-introducción)
  - [2. Papers](#pushpin2-papers)
    - [2.1. Detección del Pico R en Señales ECG Usando Yule-Walker y Análisis de Componentes Principales](#21-detección-del-pico-r-en-señales-ecg-usando-yule-walker-y-análisis-de-componentes-principales)
    - [2.2. Modeling electrocardiogram using Yule-Walker equations and kernel machines](#22-modeling-electrocardiogram-using-yule-walker-equations-and-kernel-machines)
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

### :pushpin:2. Papers
#### 2.1. Detección del Pico R en Señales ECG Usando Yule-Walker y Análisis de Componentes Principales
<center><img src="paper1.png"/></center>
<center>Figura 1: Título del paper 1 []</center>

- **Objetivo general:**
    <p align="justify">
    Analizar y aplicar técnicas de procesamiento digital, enfocadas en EMG, ECG y EEG, mediante el diseño de filtros Wavelet, con el fin de mejorar la calidad de las señales y facilitar su interpretación.
    </space>

#### 2.2. Modeling electrocardiogram using Yule-Walker equations and kernel machines
<center><img src="paper2.png"/></center>
<center>Figura 2: Título del paper 2 []</center>

  - **Objetivos:**
    - <p align="justify">Revisar y comparar las técnicas de diseño de filtros Wavelet.
    - <p align="justify">Implementar los filtros en señales EMG, ECG y EEG, para evaluar su desempeño en la reducción de ruido sin pérdida de información fisiológica relevante.
    - <p align="justify">Analizar los resultados de las señales EMG, ECG y EEG filtradas.

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
7.	Welcome to [Internet]. Python.org. [citado el 20 de septiembre de 2025]. Disponible en: https://www.python.org/

### :raised_hand:Participación
- Eduardo Poma: 33.33%
- Rodrigo Gorbeña: 33.33%
- Jennifer Cancino: 33.33%