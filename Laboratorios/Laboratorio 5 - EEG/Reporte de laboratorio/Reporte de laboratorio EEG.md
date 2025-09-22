## :brain:Adquisición de señales EEG con BITalino
### :date:Tabla de contenidos

  - [1. Introducción](#page_facing_up1-introducción)
  - [2. Objetivos](#pushpin2-objetivos)
  - [3. Materiales](#pencil23-materiales)
  - [4. Metodología](#clipboard4-metodología)
    - [4.1. Conexión BITalino](#41-conexión-bitalino)
    - [4.2. Configuración OpenSignals](#42-configuración-opensignals)
    - [4.3. Colocación de electrodos](#43-colocación-de-electrodos)
    - [4.4. Video de tomas y ploteo de OpenSignals](#44-video-de-tomas-y-ploteo-de-opensignals)
  - [5. Señales](#chart_with_upwards_trend5-señales)
    - [5.1. Posición - Frente](#51-posición---frente)
      - [5.1.1 Reposo](#511-reposo)
      - [5.1.2 Resta](#512-resta)
      - [5.1.3 Parpadeo](#513-parpadeo)
      - [5.1.4 Libre](#514-libre)
  - [6. Discusión](#bookmark_tabs6-discusión)
  - [7. Conclusiones](#memo7-conclusiones)
  - [Referencias](#notebookreferencias)
  - [Participación](#raised_handparticipación)
  
### :page_facing_up:1. Introducción
<p align="justify">
El electroencefalograma (EEG) es una herramienta diagnóstica que registra la actividad eléctrica del cerebro a través de electrodos colocados en el cuero cabelludo. Su funcionamiento se basa en la detección de los potenciales eléctricos generados por la descarga sincrónica de las neuronas corticales, especialmente de las células piramidales, cuyo patrón se refleja en ondas características (alfa, beta, theta y delta) [1].

![image](https://www.frontiersin.org/files/Articles/515216/frym-08-00096-HTML/image_m/figure-1.jpg)
<center>Figura 1: Bandas de frecuencia EEG de lenta a rápida. [2]</center>

<p align="justify">

La identificación de señales EEG es importante en el ambiente clínico, ya que permite identificar y evaluar crisis epilépticas, diferenciar condiciones que pueden simularlas, clasificar tipos de convulsiones y valorar el estado de pacientes en coma o con encefalopatías [3]. 
<p align="justify">
En este escenario, se vuelve necesario disponer de herramientas que posibiliten el registro, procesamiento y análisis de señales EEG de forma práctica y confiable. Una alternativa que responde a esta necesidad es BITalino, un sistema económico y de código abierto diseñado para la adquisición de bioseñales. Este equipo integra sensores modulares y un software propio (OpenSignals), lo que permite medir señales como EEG, EMG, ECG, EDA, entre otras, resultando útil para contextos educativos y de laboratorio [4].
<p align="justify">
En este informe se hace uso del hardware BITalino, en conjunto con su kit de herramientas y software OpenSignals, para registrar las señales EEG de un compañero de laboratorio, con el propósito de analizar e identificar los patrones eléctricos vinculados a la contracción cardíaca.

### :pushpin:2. Objetivos
- **Objetivo general:**
  <p align="justify">
  Adquirir, registrar y analizar señales biomédicas de electroencefalograma (EEG)  mediante el uso del módulo BITalino y el software OpenSignals, con el fin de comprender los principios de adquisición de bioseñales y su procesamiento básico en aplicaciones clínicas y tecnológicas.
</space>

- **Objetivos específicos:**
    
  - <p align="justify">Registrar señales biomédicas de electroencefalograma (EEG) empleando el módulo BITalino.
  - <p align="justify">Configurar el dispositivo BITalino y establecer su conexión con el software OpenSignals (r)evolution para garantizar una adquisición correcta de datos
  - <p align="justify">Obtener y exportar la información de las señales EEG desde el software, con el propósito de realizar su procesamiento y análisis posterior.

### :pencil2:3. Materiales
- **Hardware:**

    | Nombre | Cantidad | Descripción | Ilustración |
    |--------|----------|-------------|-------------|
    | **Laptop** | 1 | Computador portátil y compacto que integra pantalla, teclado y batería, sistema operativo de 64 bits. | ![image](https://intercompras.com/images/product/ACER_NH.Q2MAL.001.jpg) |
    | **BITalino** | 1 | Dispositivo modular de adquisición biomédica que registra señales fisiológicas mediante electrodos de superficie. | ![image](https://www.pluxbiosignals.com/cdn/shop/products/BITalino-Plugged-Board.1.jpg) |
    | **Electrodos** | 3 | Sensores circulares de un solo uso con adhesivo y gel conductor, ideales para captar señales bioeléctricas (ECG, EMG, EEG). | ![image](https://mecatronica.saisac.pe/wp-content/uploads/2024/10/ELECTRODO.png) |
    | **Cable** | 1 | Cable de 3 electrodos Ag/AgCl. Accesorio que facilita la captura y transmisión de las señales con baja interferencia. | ![image](https://mecatronica.saisac.pe/wp-content/uploads/2024/10/CABLEELECTRODO.png) |
    | **Batería** | 1 | Batería de litio recargable de 3.7 V. Fuente de energía, usada para alimentar el BITalino. | ![image](https://www.engitronicperu.com/wp-content/uploads/BATL.jpeg) |
    
<center>Tabla 1: Hardware [5, 6, 7]</center>

- **Software:**

    | Nombre | Cantidad | Descripción | Ilustración |
    |--------|----------|-------------|-------------|
    | **OpenSignals** | 1 | Software oficial de BITalino para la adquisición y visualización en tiempo real de las señales fisiológicas. | ![image](https://cdn.shopify.com/s/files/1/0595/1068/5887/t/6/assets/ezgif5b55a161ca2-1-1-1649945010655.png?v=1649945012) |
    | **Python** | 1 | Lenguaje de programación con múltiples librerías en ciencia de datos y procesamiento de señales. | ![image](https://scratchpad.co.nz/wp-content/uploads/2020/07/learn-python-scaled.jpeg) |
<center>Tabla 2: Software [8, 9]</center>

### :clipboard:4. Metodología
#### 4.1. Conexión BITalino
<p align="justify">
Primero se alimenta el dispositivo BITalino con la bateria de litio de 3.7 V.
<center><img src="https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%205%20-%20EEG/Extras/Bateria.gif?raw=true" width="200" height="350"/></center>
<center>Figura 2: Alimentación BITalino [Elaboración propia]</center>
Luego, se utilizó el canal EEG (A4) de la placa Bitalino 6D-86, conectando el cable con 3 electrodos Ag/AgCl circulares como se muestra a continuación.

<center><img src="https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%205%20-%20EEG/Extras/Canal.gif?raw=true" width="200" height="350"/></center>
<center>Figura 3: Conexión ECG BITalino [Elaboración propia]</center>

#### 4.2. Configuración OpenSignals
Primero, realizamos la conexión Bluetooth con el BITalino.
<center><img src="https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%205%20-%20EEG/Extras/Bluetooth.gif?raw=true" width="400" height="200"/></center>
<center>Figura 4: Conexión Bluetooth [Elaboración propia]</center>

Luego, se ingresa al software OpenSignals (r)evolution.
<center><img src="https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%205%20-%20EEG/Extras/Inicio.gif?raw=true" width="400" height="200"/></center>
<center>Figura 5: Ingresando a OpenSignals [Elaboración propia]</center>

<p align="justify">
Abrimos el administrador de dispositivos de Opensignals (r)evolution para acceder y configurar nuestro BITalino.

<center><img src="https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%205%20-%20EEG/Extras/Verde.gif?raw=true" width="400" height="200"/></center>
<center>Figura 6: Administrador de dispositivos [Elaboración propia]</center>

<p align="justify">
Seleccionamos el BITalino haciendo clic en el botón ENABLED. El dispositivo estara activado si el botón ENABLED está en azul.

<center><img src="https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%205%20-%20EEG/Extras/Enabled.gif?raw=true" width="400" height="200"/></center>
<center>Figura 7: Activando el BITalino [Elaboración propia]</center>

<p align="justify">
Hacemos clic en el logotipo de BITalino para acceder a su configuración. En el menú desplegable seleccionamos solo el canal EEG (A4) y deseleccionamos todos los demás. Además, configuramos su frecuencia de muestreo en 1000 Hz.

<center><img src="https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%205%20-%20EEG/Extras/Confi.gif?raw=true" width="400" height="200"/></center>
<center>Figura 8: Configurando el BITalino [Elaboración propia]</center>

<p align="justify">
Activamos el canal de adquisición haciendo clic en el círculo rojo (grabar).

<center><img src="https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%205%20-%20EEG/Extras/Grabar.gif?raw=true" width="400" height="200"/></center>
<center>Figura 9: Adquisición de la señal [Elaboración propia]</center>

#### 4.3. Colocación de electrodos
<p align="justify">
El siguiente procedimiento consiste en colocar los electrodos EEG en el usuario. Para ello se utilizó la Home Guide 3 - EEG del repertorio BITalino Lab Guides (Home Guides) [10].
Primero, retiramos la lámina protectora del electrodo antes de colocarlo en la piel.

<center><img src="https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%205%20-%20EEG/Extras/Despegar.gif?raw=true" width="200" height="350"/></center>
<center>Figura 10: Retiro de lámina protectora [Elaboración propia]</center>

Colocamos el electrodo de referencia (tierra) en la región del mastoide, detrás de la oreja.
<center><img src="https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%205%20-%20EEG/Extras/Tierra.gif?raw=true" width="200" height="350"/></center>
<center>Figura 11: Electrodo de referencia [Elaboración propia]</center>

Por último, colocamos los electrodos activos en las posiciones Fp1 y Fp2 de la frente.
<center><img src="https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%205%20-%20EEG/Extras/Fp1.gif?raw=true" width="400" height="200"/></center>
<center>Figura 12: Electrodos activos Fp1 [Elaboración propia]</center>
<center><img src="https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%205%20-%20EEG/Extras/Fp2.gif?raw=true" width="400" height="200"/></center>
<center>Figura 13: Electrodos activos Fp2 [Elaboración propia]</center>

#### 4.4. Video de tomas y ploteo de OpenSignals
- Posición - Frente: 
  Se tomaron las siguientes señales:
  - Reposo: primero se tomo el reposo con los ojos abiertos por 30 segundos, para que luego el sujeto fijara la vista en un objeto por 1 minuto y finalmente volver al reposo con los ojos cerrados durante 30 segundos, se tomaron 3 repeticiones de este ejercicio.

  | Ojos abiertos | Fijación de vista | Ojos cerrados |
  |---------------|-------------------|---------------|
  |[![alt text](image.png)](https://youtu.be/1qJOuY2MASQ)| [![alt text](image-2.png)](https://youtu.be/8_Lt5MzyNQ4)| [![alt text](image-1.png)](https://youtu.be/yNSh1gRJsFM) |
  <center>Tabla 3: Videos de los diferentes momentos en reposo [Elaboración propia]</center>

  - Resta: se le pidio al usuario que reste, mental y sucesivamente, 7 desde el número 100; se tomó una sola repetición de este ejercicio.
    <center><video controls src="https://youtu.be/wDPcftfDTB8" title="Title"></video></center>
    <center>Figura 14: Video de la señal cuando se resta [Elaboración propia]</center>

  - Parpadeo: el usuario parpadeaba cada dos segundos durante un minuto, se tomaron 3 repeticiones de este ejercicio.
    <center><video controls src="https://youtu.be/HB1uzi7vyeU" title="Title"></video></center>
    <center>Figura 15: Video de la señal cuando se parpadea [Elaboración propia]</center>

  - Libre: el usuario primero escucho una canción agradable, para su persona, por 2 minutos, luego, se emitio una canción que no era de su agrado por otros 2 minutos; se realizo una sola toma por canción en este ejercicio.
  
  | Música agradable | Música desagradable |
  |------------------|---------------------|
  | [![alt text](image-3.png)](https://youtu.be/kQsZQR4eNWY)| [![alt text](image-4.png)](https://youtu.be/uA0cUJQFUVI) |
<center>Tabla 4: Videos de los dos tipos de música [Elaboración propia]</center>

### :chart_with_upwards_trend:5. Señales
#### 5.1. Posición - Frente
##### 5.1.1. Reposo:
  A continuación se muestran las señales EEG filtradas correspondientes a la toma 1 para las tres condiciones de reposo: ojos abiertos, fijar vista y ojos cerrados. Se emplea únicamente esta toma como ejemplo gráfico para ilustrar de manera representativa la morfología temporal de la señal, dado que mostrar las tres repeticiones simultáneamente dificultará la claridad visual; sin embargo, el análisis cuantitativo posterior se realizó sobre las tres tomas.
  - Reposo con los ojos abiertos:
  ![image](https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%205%20-%20EEG/Extras/OA.png?raw=true)
  <center>Figura 16: Señales EEG cuando se esta en reposo con los ojos abiertos. [Elaboración propia]</center>
  <p align="justify">
  Durante la condición de ojos abiertos la señal presenta oscilaciones de baja amplitud, más o menos irregulares, con la aparición de picos esporádicos que pueden ser asociado a artefactos fisiológicos como el paradero o micro contracciones musculares. Lo visto en la gráfica es coherente con lo que describe la literatura, donde el estado de ojos abiertos tiene por característica principal la supresión relativa del ritmo alfa debido a la entrada visual constante u a la mayor activación cortical y occipital [11]. 

  - Mirada fija en un objeto:
  ![image](https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%205%20-%20EEG/Extras/FV.png?raw=true)
  <center>Figura 17: Señales EEG cuando se fija la mirada. [Elaboración propia]</center>
  <p align="justify">
  En la condición de fijación de vista se observa el aumento de la variabilidad de la amplitud y una mayor presencia de deflexiones marcas en comparación con la de solo ojos abiertos. Este comportamiento puede ser explicado a través de la atención visual sostenida y la reducción voluntaria de los párpados, lo cual modifica la dinámica de la acogida cortical y tiende a desplazar el equilibrio hacia frecuencia más rápidas(control atencionales mantenido). En recientes estudios se confirma que este estado representa un punto intermedio entre el reposo con ojos cerrados y tareas cognitivas mostrando patrones parciales de organización funcional [11].

  - Reposo con los ojos cerrados:
  ![image](https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%205%20-%20EEG/Extras/OC.png?raw=true)
  <center>Figura 18: Señales EEG cuando se esta en reposo con los ojos cerrados. [Elaboración propia]</center>
  <p align="justify">
  En lo que corresponde a los ojos cerrados, se evidencian  oscilaciones rítmicas y de mayor amplitud, que sufren una mayor sincronización cortical. Este fenómeno corresponde a la activación del ritmo alfa occipital que es típica del reposo con ausencia de estimulación visual. Tal como se ha documentado, la potencia relativa en el alfa es significativamente mayor en ojos cerrados que en ojos abiertos [12], y se ha consolidado la interpretación de este ritmo como un marcador de inhibición cortical y estado de reposo sensorial [13].

  - Ánalisis Estadístico:
  ![image](https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%205%20-%20EEG/Extras/PSDR.png?raw=true)
  <center>Figura 19: Densidad espectral de potencias (PSD). [Elaboración propia]</center>
  <p align="justify">
  En la imagen se muestra la densidad espectral de potencias (PSD) calculada mediante el método welch (ventana de 2 segundos) y promediada sobre las tres tomas realizada en la condición de reposo, La región sombreada indica la banda alfa (8-12 Hz). Se observa que, en la condición de ojos cerrados (verde), la banda alfa se mantiene ligeramente por encima de la correspondiente a ojos abiertos (azul) y fijación de vista (anaranjado), esto sugiere un ncmr lot relativo de potencia alfa al cerrar los ojos. Pero, la magnitud de la indefensión es pequeña y la superposición de las curvas refleja la variabilidad de los datos. Por ello, se usó el promedio para poder buscar la tendencia general y evitar el ruido visual que implicaría mostrar las tres repeticiones por separado. 

  ![image](https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%205%20-%20EEG/Extras/BandaR.png?raw=true)
  <center>Figura 20: Resumen cuantitativo de la potencia en la banda alfa. [Elaboración propia]</center>
  <p align="justify">
  En la figura se resume cuantitativamente la potencia integrada en la banda alfa (barras promedio error estándar de la media SEM). Los resultados muestran un aumento prpgresivo desde ojos abiertos (1.7 µV²), fijación vista (3.0 µV²) y ojos cerrados (3.6 µV²). Esta tendencia coincide con lo esperado: el cierre ocular induce una sincronización occipital alfa más marcada, mientras que la fijación visual representa un estado intermedio de activación atencional que reduce parcialmente dicha oscilación. Lo encontrado en el laboratorio concuerda con algunos estudios que reportan mayor potencia alfa en reposo con ojos cerrados respecto a ojos abiertos [12], además, se describe la fijación como un estado funcional distinto, con cambios específicos en la organización de redes cerebrales [11].
  
  Resultados de la prueba t pareada:
    <center> T-test pareado α (Abiertos vs Cerrados): t=-0.95, p=0.4436 </center>

  Sin embargo, al aplicar la prueba t pareada entre ojos abiertos y cerrados, la diferencia no alcanzó significancia estadística (p > 0.05). Esta diferenciación con lo descrito en la literatura se puede atribuir a factores, metodológicos: tamaño de la muestras reducida, ubicación de los electrodos, y la presencia de artefactos fisiológicos que aumentan la variabilidad entre las diferentes tomas. Revisiones recientes señalan que los estados de reposo con ojos abiertos y cerrados no deben considerarse equivalentes, y que su comparación exige cuidado metodológico y mayor control experimental [13].

##### 5.1.2. Resta:
  - Tarea cognitiva:
  <center><img src="https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%205%20-%20EEG/Extras/R.png?raw=true"/></center>
  <center>Figura 21: Señales EEG cuando se realiza una tarea cognitiva. [Elaboración propia]</center>
  <p align="justify">
  En la figura se presenta la señal EEG filtrada (1-40 Hz) durante la condición de tarea cognitiva en la que el participante realizó una operación de restar de 7 en 7 desde 100. Se observa una señal de aproximadamente 70 segundos con oscilaciones moderadas que rondan los ±20 µV y presencia de algunas deflexiones abruptas. Las deflexiones pueden estar asociadas a artefactos fisiológicos (parpadeos, micro contracciones musculares) o también a pico de activación cortical que están relacionadas con la carga cognitiva. En general, la señal presenta mayor variabilidad en comparación con el estado de reposo, lo que concuerda con el incremento en el reclutamiento de recursos neurales durante tareas que demandan atención y memoria de trabajo [14, 15].

  - Toma de 30 segundos en reposo:
  <center><img src="https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%205%20-%20EEG/Extras/30R.png?raw=true"/></center>
  <center>Figura 22: Segmento de la señal EEG cuando se esta en reposo con los ojos abiertos. [Elaboración propia]</center>
  <p align="justify">
  En contraste, la figura 22 muestra un segmento de 30 segundos de una de las tomas de reposo con ojos abiertos, utilizando como condición basal para comparación. La señal presenta oscilación de menor amplitud (exceptuando por algunos picos) y menor variabilidad en relación con la condición de tarea. Esta diferencia sugiere un mayor nivel de sincronización y menor demanda de procesamiento en reposo, lo que concuerda con lo que se ha reportado para estados bajo carga cognitiva [14]. 

  - Ánalisis Estadístico:
  ![image](https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%205%20-%20EEG/Extras/PSDResta.png?raw=true)
  <center>Figura 23: Densidad espectral de potencias (PSD). [Elaboración propia]</center>
  <p align="justify">
  En la figura 23 se muestran las curvas de densidad espectral de potencia obtenidas mediante el método de welch para la condición de reposo con ojos abiertos (promedio de tres tomas) Y para la tarea cognitiva (única toma). La región sombreada corresponde a la branda Beta (13-30Hz). Se observa que la curva de la tarea no presenta un claro incremento en Beta con respecto al reposo, sino que por el contrario, la PSD de la tarea se sitúa por debajo de la condición basal en gran parte de esta banda. 

  ![image](https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%205%20-%20EEG/Extras/BandaResta.png?raw=true)
  <center>Figura 24: Resumen cuantitativo de la potencia en la banda alfa. [Elaboración propia]</center>
  Potencia β (13–30 Hz):
  <center>Reposo (promedio 3 tomas): 2.4360 µV²  (SEM = 0.6056)</center>
  <center>Tarea (única toma): 1.8775 µV²</center>
  <center>Diferencia absoluta (Tarea - Reposo): -0.5585 µV²</center>
  <center>Cambio relativo: -22.93 %  (positivo = Tarea > Reposo)</center>

  <p align="justify">En la figura 24 se resume cuantitativamente la potencia integrada en Beta para ambas condiciones. El promedio en reposo fue de 2.44 µV² (SEM = 0.61), mientras que la tarea cognitiva registró un valor de 1.88 µV². Esto representa una diferencia absoluta de –0.56 µV² y un cambio relativo de –22.9 %. Lo que se eocntró resulta inesperado pues en la literatura se describe un cinremende otenicna en Bet dutantwa tareas de atención, memoria de trabajo a cálculos mentales [14 - 16].

##### 5.1.3. Parpadeo:
  <center><img src="https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%205%20-%20EEG/Extras/P.png?raw=true"/></center>
  <center>Figura 25: Tomas de las señales ECG cuando se realiza un parpadeo constante. [Elaboración propia]</center>
  <p align="justify">
  En las tres tomas de un minuto cada una, la detección de parpadeos con el criterio ±80 µV detecto 0 eventos en todos los casos. Esto se explica porque el módulo EEG de BITalino presenta un rango de entrada de ±39.49 µV [17], lo que imposibilita registrar señales de amplitud superior a este umbral.
  <p align="justify">
  Cuando se aplicó un umbral adaptativo basado en MAD (k=8), se logró identificar 15 parpadeos en la primera toma mientras en que en la segunda y tercera toma se decto 1 y 2 para cada una, respectivamente. En T1 el resultado se aproxima al protocolo experimental (un parpadeo cada 2 s = 30 parpadeos/min), mientras que en T2 y T3 el conteo fue muy inferior. El umbral adaptativo calculado para cada registro osciló entre 22 y 39 µV.
  <p align="justify">
  El resultado de no detectar ningún evento con el criterio de 80 µV confirma que este umbral es incompatible con la limitaciones del BITalino EEG. En condiciones clínicas y con electrodos EOG delicados, los parpadeos pueden alcanzar 100-200 uV [18]. En, cambio en sistemas como el BITalino, portátiles y de bajo rango, la amplitud máxima detectable se restringe a decenas de microvoltios, por lo que or lo que el criterio de la guía (parpadeos >80 µV) no puede cumplirse. Los resultados de la toma 1 muestran que  el método adaptativo permite recuperar la dinámica de los parpadeos y aproximarse al protocolo experimental, aun como amplitudes reducidas. Sin embargo, en las tomas 2 y 3 la detección fue muy baja, lo que sugiere problemas adicionales como impedancias elevadas, variabilidad en la ejecución de los parpadeos o ruido de contacto. Estudios recientes sobre EEG en dispositivos vestibles destacan precisamente que la variabilidad intersesión y las condiciones del montaje suelen afectar la eficacia de la detección de artefactos, por ello se recomienda el uso de umbrales adaptativos frente a valores fijos [19], [20].

##### 5.1.4. Libre:
  - Ánalisis Estadístico:
  ![image](https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%205%20-%20EEG/Extras/PSDM.png?raw=true)
  <center>Figura 26: Densidad espectral de potencias (PSD). [Elaboración propia]</center>
  <p align="justify">
  La estimación espectral mediante el método Welch es adecuada para este análisis, pues reduce la varianza de la PSD y permite hacer comparaciones  en condiciones de forma robusta en EEG [21, 22]. En la figura, las curvas correspondientes a música que gusta y música que no sugiere se superen ampliamente en la mayor del rango 0-40 Hz, sin un cio alfa marcado, lo que sugiere que las no existen muchas diferencias globales.
  <p align="justify">
  Además, se observa un leve predominio de potencia en la banda  β (13–30 Hz) durante MG respecto a MNG.  Este hallazgo aunque sutil es compatible con lo descrito en estudios recientes en relación la música placentera con incrementen la actividad de bandas β y γ frontales, asociado a proceso de recompensa y predicción en la experiencia musical [23].  No obstante, debido al uso de un solo canal y a la variabilidad individual, el resultado debe interpretarse con cautela.
  <p align="justify"> 
  Los resultados de la integración espectral muestran que la potencias en bandas  θ, α y β fue notablemente mayores durante la condición de música que gusta frente a la de música que no gusta. En especial se observó aumento de 0.319 µV² en θ, 0.085 µV² en α y 0.463 µV² en β. Estos incrementos (modestos) confirman la tendencia ya sugerida en la curva de PSD estimada en Welch, que es un método robusto y ampliamente utilizado en el análisis de señales EEG [21, 22].

  ![image](https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%205%20-%20EEG/Extras/BandaM.png?raw=true)
  <center>Figura 27: Resumen cuantitativo de las potencias de bandas theta, alfa y beta. [Elaboración propia]</center>
  <p align="justify">
  En la comparación de potencia por bandas refuerza los hallazgos observados en la PSD. En todas las frecuencias analizadas, la condición de música que gusta presto valores superiores(aunque ligeramente) respecto a la música que no gusta:  θ = 2.717 vs. 2.398 µV², α = 1.320 vs. 1.235 µV² y β = 2.464 vs. 2.001 µV².
  <center>Engagement β/(α+θ):  MG=0.610   MNG=0.551   Δ=-0.060</center>
  <p align="justify">
  El incidente egagamente  β/(α+θ) mostró, también, una diferencia favorable hacia la musica que gusta (0.610 vs. 0.551), lo que coincide con la literal que valida este pareto como un marcador de compromiso y atención en tareas cognitivas y estímulos sensoriales [24], [25].
  <p align="justify">
  En conjunto, los datos sugieren que la música que es de mayor gusto induce una mayor activación cortical y un estado de mayor implicación atencional, aunque la magnitud del efecto es modesta y debe interpretarse dentro de las limitaciones de un registro con un solo canal y un único sujeto.


### :bookmark_tabs:6. Discusión
- **¿Qué banda de frecuencia predomina al cerrar los ojos?**
  <p align="justify">Cuando se realizo el análisis de reposo, se observó un incremento en la potencia alfa (8–12 Hz) al cerrar los ojos, esto indica que la actividad cortical esta en relajación y con un menor procesamiento visual [11]–[13]. Aunque en este laboratorio la diferencia no alcanzó significancia estadística, podemos confirma por la literatura que el ritmo alfa se encuentra predominante en esta condición, siendo así la banda que se espera observar con mayor claridad.
- **¿Qué filtro es imprescindible para EEG y por qué?**
  <p align="justify">Para el procesamiento de señales EEG, el filtrado pasa banda es necesario para aislar las oscilaciones de interés y atenuar tanto las componentes de baja frecuencia como el ruido en alta frecuencia. Para nuestro trabajo se empleó un filtro pasa banda de 1 a 40 Hz, lo cual es recomendado para eliminar artefactos de movimiento y evitar interferencias de red eléctrica [21], [22].
- **¿Puedes modular conscientemente tu señal EEG? Da un ejemplo.**
  <p align="justify">Es posible influir conscientemente en ciertas bandas con tareas cognitivas. Por ejemplo, durante la resolución de la tarea matemática se esperaba un incremento en β, banda asociada a atención y memoria de trabajo [14]–[16]. Si bien en nuestra toma no se observó con claridad, estudios demuestran que incrementar la concentración puede modificar deliberadamente la potencia de estas bandas.
- **¿Se observan diferencias entre Fp1 y Fp2? ¿Por qué podrían ocurrir?**
  <p align="justify">En nuestro experimento no se pudo registrar simultáneamente ambos canales, pero según lo encontrado en la literatura pueden observarse diferencias debido a la asimetría frontal (FAA), asociada a procesos emocionales [23]. Por ejemplo, mayor supresión de alfa en el hemisferio izquierdo se ha vinculado a emociones positivas, mientras que en el derecho a emociones negativas [23], [24]. Esta asimetría es sensible a condiciones como la música, el estado de ánimo y la carga cognitiva, y explicaría por qué Fp1 y Fp2 pueden diferir en amplitud.

### :memo:7. Conclusiones
<p align="justify">
En el trabajo se realizaron distintos análisis de señales EEG en condiciones de reposo, tareas cognitivas y estímulos musicales, utilizando como base el método WElch para estimaciones espectral. Los resultado en ipsos mostraron la tenencia esperada que un aumento progresivo de la potencian alfa desde ojos abierto hasta los ojos cerrados, pero sin alcanzar bases  estadísticas significativas, esto probablemente debido al tamaño reducido de la muestras y la interrupción de artercatos fisiológico [12, 13].
<p align="justify">
En la tarea cognitiva, se pudo observar una disminución de la potencia en la banda beta respecto al reposo, esto contrasta con lo que se ha reportado en la literatura donde se describe un incremento de estas actividad en contexto de gran atención y memoria de trabajo [15, 16]. Es posible que el hecho de tener una sola toma, el emplazamiento de los electrodos y la intervención de artefactos hayan sido partícipes de la discrepancia.
<p align="justify">
En el análisis de artefactos de parpadeo, se evidencio que el umbral absoluto  ±80 µV que se propuso en la guía no es compatible con las limitaciones intrínsecas del sensor BITalino (±39.49 µV) [17]. Por ello, se usó la aplicación de un umbral adaptativo basado en MAD que permitió detectar parpadeos de manera más realista; sin embargo, con gran variabilidad entre tomas, en concordancia con lo reportado en estudios sobre EEG vestible [18, 19].
<p align="justify">
Por último,  en la comparación entre música que gusta y que no gusta se observó un incremento ligero en  θ, α y especialmente en β para la condición de mayor agrado, que fue acompañado de un ligero aumento ene l indice de  engagement β/(α+θ). En conjunto, estos resultados, aunque preliminares , son compatibles con investigaciones qué relacionan la música placentera con mayor activación cortical y participación de redes de recompensa [21, 25].

### :notebook:Referencias
<p align="justify">
1. Rayi A, Murr NI. Electroencephalogram. En: StatPearls. Treasure Island (FL): StatPearls Publishing; 2025.

<p align="justify">
2. van Atteveldt N, Janssen TWP, Davidesco I. Measuring brain waves in the classroom. Front Young Minds [Internet]. 2020;8. Disponible en: http://dx.doi.org/10.3389/frym.2020.00096

<p align="justify">
3. Jadhav C, Kamble P, Mundewadi S, Jaiswal N, Mali S, Ranga S, et al. Clinical applications of EEG as an excellent tool for event related potentials in psychiatric and neurotic disorders. Int J Physiol Pathophysiol Pharmacol. 2022;14(2):73–83.

<p align="justify">
4. Wagner RE, Plácido da Silva H, Gramann K. Validation of a low-cost electrocardiography (ECG) system for psychophysiological research. Sensors (Basel) [Internet]. 2021;21(13):4485. Disponible en: http://dx.doi.org/10.3390/s21134485

<p align="justify">
5. BITalino [Internet]. PLUX Biosignals. [citado el 20 de septiembre de 2025]. Disponible en: https://www.pluxbiosignals.com/collections/bitalino?srsltid=AfmBOoqBigYX8r0j9zwN0ihDuDh8aKeExNMqrqEBD33tRp62ois9JYyd

<p align="justify">
6. CABLE PARA 3 ELECTRODOS – EMG/ECG [Internet]. Saisac.pe. [citado el 20 de septiembre de 2025]. Disponible en: https://mecatronica.saisac.pe/producto/cable-para-3-electrodos-emg-ecg-2

<p align="justify">
7. Batería de litio 3.7 V [Internet]. Engitronicperu.com. [citado el 20 de septiembre de 2025]. Disponible en: https://www.engitronicperu.com/producto/bateria-de-litio-3-7-v

<p align="justify">
8. Insights that connect you to success [Internet]. Opensignal.com. [citado el 20 de septiembre de 2025]. Disponible en: https://www.opensignal.com/

<p align="justify">
9. Welcome to [Internet]. Python.org. [citado el 20 de septiembre de 2025]. Disponible en: https://www.python.org/

<p align="justify">
10. Biosignals P. BITalino lab guides (home guides) [Internet]. Pluxbiosignals.com. 2022 [citado el 20 de septiembre de 2025]. Disponible en: https://support.pluxbiosignals.com/knowledge-base/bitalino-lab

<p align="justify">
11. Krukow P, Rodríguez-González V, Kopiś-Posiej N, Gómez C, Poza J. Tracking EEG network dynamics through transitions between eyes-closed, eyes-open, and task states. Sci Rep [Internet]. 2024;14(1):17442. Disponible en: http://dx.doi.org/10.1038/s41598-024-68532-2


<p align="justify">
12. Petro NM, Ott LR, Penhale SH, Rempe MP, Embury CM, Picci G, et al. Eyes-closed versus eyes-open differences in spontaneous neural dynamics during development. Neuroimage [Internet]. 2022;258(119337):119337. Disponible en: http://dx.doi.org/10.1016/j.neuroimage.2022.119337

<p align="justify">
13. Pascucci D, Menétrey MQ, Passarotto E, Luo J, Paramento M, Rubega M. EEG brain waves and alpha rhythms: Past, current and future direction. Neurosci Biobehav Rev [Internet]. 2025;176(106288):106288. Disponible en: http://dx.doi.org/10.1016/j.neubiorev.2025.106288

<p align="justify">
14. Chikhi S, Matton N, Blanchet S. EEG power spectral measures of cognitive workload: A meta-analysis. Psychophysiology [Internet]. 2022;59(6):e14009. Disponible en: http://dx.doi.org/10.1111/psyp.14009
<p align="justify">
15. Lundqvist M, Miller EK, Nordmark J, Liljefors J, Herman P. Beta: bursts of cognition. Trends Cogn Sci [Internet]. 2024;28(7):662–76. Disponible en: http://dx.doi.org/10.1016/j.tics.2024.03.010
<p align="justify">
16.	Palacios-García I, Silva J, Villena-González M, Campos-Arteaga G, Artigas-Vergara C, Luarte N, et al. Increase in beta power reflects attentional top-down modulation after psychosocial stress induction. Front Hum Neurosci [Internet]. 2021;15:630813. Disponible en: http://dx.doi.org/10.3389/fnhum.2021.630813

<p align="justify">
17. PLUX biosignals [Internet]. PLUX Biosignals. [citado el 20 de septiembre de 2025]. Disponible en: http://bitalino.com/
<p align="justify">
18.	Wang J, Cao J, Hu D, Jiang T, Gao F. Eye blink artifact detection with novel optimized multi-dimensional electroencephalogram features. IEEE Trans Neural Syst Rehabil Eng [Internet]. 2021;29:1494–503. Disponible en: http://dx.doi.org/10.1109/TNSRE.2021.3099232
<p align="justify">
19.	Zhang G, Luck SJ. Assessing the impact of artifact correction and artifact rejection on the performance of SVM-based decoding of EEG signals [Internet]. bioRxivorg. 2025. Disponible en: http://dx.doi.org/10.1101/2025.02.22.639684
<p align="justify">
20.	Arpaia P, De Luca MD, Di Marino LD, Duran D, Gargiulo L, Lanteri P, et al. A systematic review of techniques for artifact detection and artifact category identification in electroencephalography from wearable devices. Sensors (Basel) [Internet]. 2025;25(18):5770. Disponible en: http://dx.doi.org/10.3390/s25185770

<p align="justify">
21.	Zhang H, Zhou Q-Q, Chen H, Hu X-Q, Li W-G, Bai Y, et al. The applied principles of EEG analysis methods in neuroscience and clinical neurology. Mil Med Res [Internet]. 2023;10(1):67. Disponible en: http://dx.doi.org/10.1186/s40779-023-00502-7

<p align="justify">
22.	Chiu C-A, Lu M-C, Zhong Y-L, Tsai T-Y, Liu C-J, Ho M-C. Quantifying and analyzing brainwave electroencephalography with Welch’s method. Sens Mater [Internet]. 2023;35(5):1579. Disponible en: http://dx.doi.org/10.18494/sam4065

<p align="justify">
23.	Ueno F, Shimada S. Neural mechanism of musical pleasure induced by prediction errors: An EEG study. Brain Sci [Internet]. 2024;14(11). Disponible en: http://dx.doi.org/10.3390/brainsci14111130

<p align="justify">
24.	Ahmed Y, Ferguson-Pell M, Adams K, Ríos Rincón A. EEG-based engagement monitoring in cognitive games. Sensors (Basel) [Internet]. 2025;25(7). Disponible en: http://dx.doi.org/10.3390/s25072072

<p align="justify">
25.	Raufi B, Longo L. An evaluation of the EEG alpha-to-theta and theta-to-alpha band ratios as indexes of mental workload. Front Neuroinform [Internet]. 2022;16:861967. Disponible en: http://dx.doi.org/10.3389/fninf.2022.861967

### :raised_hand:Participación
- Eduardo Poma: 33.33%
- Rodrigo Gorbeña: 33.33%
- Jennifer Cancino: 33.33%