## :wave:Adquisición de señales EMG con BITalino
### :date:Tabla de contenidos

  - [1. Introducción](#page_facing_up1-introducción)
  - [2. Objetivos](#pushpin2-objetivos)
  - [3. Materiales](#pencil23-materiales)
  - [4. Procedimiento](#clipboard4-procedimiento)
    - [4.1. Conexión BITalino](#41-conexión-bitalino)
    - [4.2. Configuración OpenSignals](#42-configuración-opensignals)
    - [4.3. Colocación de electrodos](#43-colocación-de-electrodos)
    - [4.4. Video de tomas y ploteo de OpenSignals](#44-video-de-tomas-y-ploteo-de-opensignals)
  - [5. Resultados](#bookmark_tabs5-resultados)
    - [5.1. Posición I - Brazo](#51-posición-i---brazo)
    - [5.2. Posición II - Antebrazo](#52-posición-ii---antebrazo)
    - [5.3. Posición III - Dedo](#53-posición-iii---dedo)
  - [Referencias](#notebookreferencias)
  - [Participación](#raised_handparticipación)
  
### :page_facing_up:1. Introducción
<p align="justify">
La contracción muscular se explica cómo la interacción de los filamentos de actina y miosina. Cuando un potencial de acción alcanza la fibra muscular, se produce la liberación de iones de calcio desde el retículo sarcoplásmico. El calcio se une a la troponina, lo que desplaza la tropomiosina y deja expuestos los sitios activos de la actina [1]. 
La miosina forma puentes cruzados con la actina y realiza un movimiento de deslizamiento, acercando los filamentos y generando tensión dentro del sarcómero. Luego, la disminución misma del calcio intracelular interrumpe dicha interacción, dando paso a la relajación. Este proceso es la base de la señal registrada mediante electromiografía de superficie (sEMG) [1].
<p align="justify">
La electromiografía de superficie (sEMG) es una técnica no invasiva que registra la actividad eléctrica generada por los músculos durante la contracción, mediante electrodos colocados sobre la piel. El registro obtenido representa la suma de los potenciales de acción de múltiples unidades motoras, reflejando así las propiedades anatómicas y fisiológicas del músculo evaluado [2].
<p align="justify">
Es así que la sEMG ha encontrado múltiples aplicaciones en el ámbito clínico: evaluación de la función neuromuscular, monitoreo de la recuperación tras lesiones, guia de terapias físicas y analizador de patrones en fatiga muscular [3]. 
<p align="justify">
En este contexto, surge la necesidad de contar con herramientas que permitan registrar, procesar y analizar señales de sEMG de manera accesible y confiable. Uno de los instrumentos que responde a este propósito es BITalino, un sistema asequible y de código abierto para la adquisición de bioseñales. Este dispositivo incluye sensores modulares junto con un software propio (OpenSignals), que facilitan la medición de señales como ECG, EMG, EEG, EDA y otros, siendo una gran opción para entornos de laboratorio y aprendizaje [4].
<p align="justify">
En el presente informe se hace uso del hardware BITalino junto con su kit de herramientas y software OpenSignals para registrar señales de sEMG en un sujeto de prueba del laboratorio, con el fin de analizar e identificar los patrones eléctricos asociados a la contracción muscular humana en diferentes partes del tejido muscular esquelético.

### :pushpin:2. Objetivos
- **Objetivo general:**
  <p align="justify">
  Adquirir, registrar y analizar señales biomédicas de electromiografía (EMG)  mediante el uso del módulo BITalino y el software OpenSignals, con el fin de comprender los principios de adquisición de bioseñales y su procesamiento básico en aplicaciones clínicas y tecnológicas.
</space>

- **Objetivos específicos:**
    
  - <p align="justify">Registrar señales biomédicas de electromiografía (EMG) empleando el módulo BITalino.
  - <p align="justify">Configurar el dispositivo BITalino y establecer su conexión con el software OpenSignals (r)evolution para garantizar una adquisición correcta de datos
  - <p align="justify">Obtener y exportar la información de las señales EMG desde el software, con el propósito de realizar su procesamiento y análisis posterior.

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

### :clipboard:4. Procedimiento
#### 4.1. Conexión BITalino
<p align="justify">
Primero se alimenta el dispositivo BITalino con la bateria de litio de 3.7 V.
Luego, se utilizó el canal EMG (A1) de la placa Bitalino 70-FB, conectando el cable con 3 electrodos Ag/AgCl circulares como se muestra en las imagenes.

![image](https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%203%20-%20EMG/Extras/conexi%C3%B3n.png?raw=true)
<center>Figura 1: Conexión EMG BITalino [10]</center>

#### 4.2. Configuración OpenSignals
Se ingresa al software OpenSignals (r)evolution.
<center><img src="https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%203%20-%20EMG/Extras/Inicio.gif?raw=true" width="400" height="200"/></center>
<center>Figura 2: Ingresando a OpenSignals [Elaboración propia]</center>

<p align="justify">
Abrimos el administrador de dispositivos de Opensignals (r)evolution para acceder y configurar nuestro BITalino.

<center><img src="https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%203%20-%20EMG/Extras/verde.gif?raw=true" width="400" height="200"/></center>
<center>Figura 3: Administrador de dispositivos [Elaboración propia]</center>

<p align="justify">
Seleccionamos el BITalino haciendo clic en el botón ENABLED. El dispositivo estara activado si el botón ENABLED está en azul.

<center><img src="https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%203%20-%20EMG/Extras/Enabled.gif?raw=true" width="400" height="200"/></center>
<center>Figura 4: Activando el BITalino [Elaboración propia]</center>

<p align="justify">
Hacemos clic en el logotipo de BITalino para acceder a su configuración. En el menú desplegable seleccionamos solo el canal EMG y deseleccionamos todos los demás. Además, configuramos su frecuencia de muestreo en 1000 Hz.

<center><img src="https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%203%20-%20EMG/Extras/Confi.gif?raw=true" width="400" height="200"/></center>
<center>Figura 5: Configurando el BITalino [Elaboración propia]</center>

<p align="justify">
Activamos el canal de adquisición haciendo clic en el círculo rojo (grabar).

<center><img src="https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%203%20-%20EMG/Extras/Grabar.gif?raw=true" width="400" height="200"/></center>
<center>Figura 6: Adquisición de la señal [Elaboración propia]</center>

#### 4.3. Colocación de electrodos
<p align="justify">
El siguiente procedimiento consiste en colocar los electrodos EMG en el usuario de prueba. Para ello se utilizó la Home Guide 1 - EMG del repertorio BITalino Lab Guides (Home Guides) [10].
Retiramos la lámina protectora del electrodo antes de colocarlo en la piel.

<center><img src="https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%203%20-%20EMG/Extras/Despegar.gif?raw=true" width="300" height="500"/></center>
<center>Figura 6: Adquisición de la señal [Elaboración propia]</center>

Colocamos el electrodo de referencia (tierra) en la zona del codo.
<center><img src="https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%203%20-%20EMG/Extras/Tierra.gif?raw=true" width="300" height="500"/></center>
<center>Figura 7: Adquisición de la señal [Elaboración propia]</center>

Por último, colocamos los electrodos activos sobre el músculo a analizar.
<center><img src="https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%203%20-%20EMG/Extras/Colocar.gif?raw=true" width="300" height="500"/></center>
<center>Figura 8: Adquisición de la señal [Elaboración propia]</center>

#### 4.4. Video de tomas y ploteo de OpenSignals
- Posición I - Brazo:
  <p align="justify">
  En la posición I se tomo señales de reposo, contracción sin y con oposición del bíceps braquial (brazo), teniendo la conexión de tierra en el codo.

    | Brazo en reposo | Brazo sin oposición | Brazo con oposición |
    |-----------------|---------------------|---------------------|
    | [![alt text](image.png)](https://studio.youtube.com/video/7ckIHEaJcAU/edit) | [![alt text](image-1.png)](https://studio.youtube.com/video/-uEV9ff91Qg/edit) | [![alt text](image-2.png)](https://studio.youtube.com/video/l8y1Qev-9UU/edit) |
<center>Tabla 3: Videos de la posición I [Elaboración propia]</center>

- Posición II - Antebrazo:
  <p align="justify">
  En la posición II se tomo señales de reposo, contracción sin y con oposición del flexor radial del carpo (antebrazo), teniendo la conexión de tierra en el codo.

    | Antebrazo en reposo | Antebrazo sin oposición | Antebrazo con oposición |
    |-----------------|---------------------|---------------------|
    | [![alt text](image-3.png)](https://studio.youtube.com/video/4wpJltBbW5M/edit)| [![alt text](image-4.png)](https://studio.youtube.com/video/oahxS7n7Fsg/edit) | [![alt text](image-5.png)](https://studio.youtube.com/video/4lYDqMGYTh4/edit)|
<center>Tabla 4: Videos de la posición II [Elaboración propia]</center>

- Posición III - Dedo:
  <p align="justify">
  En la posición III se tomo señales de reposo, contracción sin y con oposición del abductor corto del pulgar, teniendo la conexión de tierra en el codo.

    | Dedo en reposo | Dedo sin oposición | Dedo con oposición |
    |-----------------|---------------------|---------------------|
    | [![alt text](image-6.png)](https://studio.youtube.com/video/TZXG5mEbC68/edit) | [![alt text](image-8.png)](https://studio.youtube.com/video/dV_JnVHRz_I/edit) | [![alt text](image-7.png)](https://studio.youtube.com/video/jzCyC5kxX8g/edit) |
<center>Tabla 5: Videos de la posición III [Elaboración propia]</center>

### :bookmark_tabs:5. Resultados
<p align="justify">
El análisis de las señales obtenidas se realiza mediante el flujo de procesamiento digital implementado en Python, que se estructuró en tres niveles: señal cruda, semal preprocesada y señal rectificada. 
<p align="justify">
En primer lugar, se importaron las señales en bruto desde los archivos generados por el sistema BITalino, seleccionando la columna que corresponde al canal EMG. Luego, se eliminó la componente DC restando la media de cada segmento. Lo anterior es necesario para que el desplazamiento de la línea base no pueda enmascarar la verdadera amplitud de la señal debido a polarizaciones de los electrodos o al hardware de adquisición [11]. 
<p align="justify">
Debido a que cada músculo y fase experimental se registró de dos a tres repeticiones, se implementó un procedimiento de alineamiento y promediado de señales, a través del recorte en la misma duración y el cálculo de un promedio punto a punto de cada repetición. Esto se hizo con el objetivo de reducir la variabilidad natural de la EMG y obtener una señal más representativa y robusta para mejorar la confiabilidad de las mediciones y reducir el error estándar [12]. 
<p align="justify">
Luego, se aplicó un filtro pasa banda entre 20 y 450 Hz debido a que la actividad eléctrica fisiológica de los músculos esqueléticos se concentran en ese rango de frecuencias, principalmente, mientras que valores por debajo de 20 Hz suelen corresponder a artefactos de movimiento y por encima de 450 Hz corresponden, predominantemente, a componentes de ruido electrónico y térmico [11]. Además, se usó un filtro notch de 60 Hz para reducir la interferencia con la red eléctrica [13]. 
<p align="justify">
Luego del filtrado, las señales se rectificaron tomando el valor absoluto de cada muestra. Tomando como base la rectificación se calculó el volvente RMS mediante una ventana para cuantificar la magnitud de la activación muscular de manera más estable y menos ruidosa [13, 14].
<p align="justify">
Finalmente, se generaron tres visualización por cada músculo y fase:  la señal promedio cruda, que permite identificar artefactos y la forma general del EMG; la señal preprocesada, donde se observa la eliminación de ruido y la preservación de la banda fisiológica; y la señal rectificada con su envolvente RMS, que cuantifica la intensidad relativa entre reposo, contracción libre y contracción con resistencia 

#### 5.1. Posición I - Brazo
- **Reposo:**
  ![image](https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%203%20-%20EMG/Extras/P1_R.png?raw=true)
  <center>fIGURA 9: Señales EMG del bíceps braquial en reposo: cruda, preprocesada y rectificada con envolvente RMS. [Elaboración propia]</center>
  <p align="justify">
  La señal se encuentra centrada en 0mV, con suaves oscilaciones distribuidas de manera irregular durante los 10 segundos de registro. La amplitud máxima no supera los ±0.2 mV, además, no se observan ráfagas de alta amplitud ni patrones repetitivos, lo que verifica la estabilidad característica de la fase de reposo. Luego de suprimir la componente DC y la aplicaciones los filtros aún se observa que la gráfica está centrada en cero pero esta vez con un rango reducido de oscilaciones, principalmente entre -0.1 a + 0.15mv, lo que indica una disminución del ruido de baja frecuencia y a preservación de la banda útil del EMG. En cuanto a la envolvente RMS, esta muestra un perfil estable con valores entre 0.015 y 0.025mV  en conjunto con algunos incrementos puntuales de hasta 0.035mV. Este comportamiento evidencia la ausencia de contracción voluntaria y la presencia de actividad basal del bíceps braquial vinculada a ruido fisiológico, fibras musculares aisladas y a la actividad eléctrica mínima de reposo. 
  <p align="justify">
  Lo que se ha reportado  es que en los músculos esqueléticos se presentan valores de  5 - 50 µV RMS (0.005 - 0.05 mV), que depende de la colocación de los electrodos,  lo que concuerda con el patrón de baja intensidad observado en esta fase [11, 14]. 


- **Movimiento sin oposición:**
  ![image](https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%203%20-%20EMG/Extras/P1_SO.png?raw=true)
  <center>Figura 10: Señales EMG del bíceps braquial sin oposición: cruda, preprocesada y rectificada con envolvente RMS. [Elaboración propia]</center>
  <p align="justify">
  Se nota un aumento evidente en la amplitud en relación con la fase de reposo. La señal sin procesar presenta pulsos más extensos y constantes, con valores que oscilan entre –0.3 y +0.25 mV. El patrón es desigual, con oscilaciones más fuertes y duraderas que interrumpen el nivel base. Al aplicar los filtros, la señal se enfoca en cero y mantiene los picos de activación, los cuales aparecen con mayor definición y amplitudes entre –0.1 y +0.15 mV, distribuidos en ráfagas durante los 10 segundos de grabación. La envolvente RMS muestra un nivel promedio superior al de reposo, oscilando entre 0.025 y 0.035 mV, con aumentos transitorios que alcanzan hasta 0.045 mV, más comunes y duraderos en relación con la fase basal. Este patrón indica el reclutamiento ocasional de unidades motoras del bíceps braquial para producir la flexión del codo sin peso adicional, dentro de una contracción dinámica de intensidad baja a moderada.
  <p align="justify">
  Lo que se ha reportado es que, en estas condiciones, la amplitud habitual de la sEMG se incrementa a 50-300 µV RMS (0.05-0.3 mV), relacionado con la activación intercalada de conjuntos de fibras musculares [11, 15]. De este modo, la señal registrada es consistente con lo anticipado para una contracción voluntaria sin oposición, marcada por picos transitorios de activación más altos que en reposo, pero aún sin llegar a la magnitud constante de una contracción máxima.


- **Movimiento con oposición:**
  ![image](https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%203%20-%20EMG/Extras/P1_CO.png?raw=true)
  <center>Figura 11: Señales EMG del bíceps braquial con oposición: cruda, preprocesada y rectificada con envolvente RMS. [Elaboración propia]</center>
  <p align="justify">
  Se aprecia un aumento muy marcado de la amplitud respecto a las fases anteriores: la señal cruda alcanza valores de hasta ±1.2 mV, con oscilaciones densas y continuas durante todo el registro. Tras aplicar el filtrado, la señal se centra en cero, manteniendo amplitudes que oscilan entre –1.0 y +1.0 mV, con un nivel de oscilación sostenido que refleja una actividad muscular más continua y uniforme en comparación con el movimiento libre. La envolvente RMS muestra un incremento estable en torno a 0.20–0.35 mV, sin descensos marcados hacia el nivel basal, lo que corresponde a una contracción mantenida de alta intensidad del bíceps braquial. Esto indica un patrón fisiológico que refleja un mayor reclutamiento de unidades motoras y el aumento en la frecuencia de descarga que son necesarias para vencer la resistencia.
  <p align="justify">
  Lo que se ha reportado es que, en contracciones intensas o cercanas al máximo, la amplitud de la sEMG puede alcanzar valores de 200 a 1000 µV RMS (0.2 - 1.0 mV), influenciado por el nivel de fuerza, la fatiga y la colocación de los electrodos [15, 16]. Se observa una concordancia entre los rangos reportados con el rango obtenido aunque no es del todo preciso. 


#### 5.2. Posición II - Antebrazo
- **Reposo:**
  ![image](https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%203%20-%20EMG/Extras/P2_R.png?raw=true)
  <center>Figura 12: Señales EMG del flexor carpi radialis en reposo: cruda, preprocesada y rectificada con envolvente RMS. [Elaboración propia]</center>
  <p align="justify">
  En la señal cruda se observa que la oscilación está centrada en torno a 0 mV, con fluctuaciones pequeñas que no superan ±0.15 mV y un patrón irregular que se mantiene durante los 10 segundos de registro. Luego del preprocesamiento, se observa que la señal se estabiliza alrededor de cero con un rango de oscilaciones más reducido, lo que refleja la disminución de ruido y la preservación de la banda fisiológica del EMG. En cuanto a la envolvente RMS, se observa que presenta valores bajos en torno a 0.015 - 0.020 mV y un pico inicial cercano a 0.040 mV(este valor  parece ser un error en la toma de la señal en el tiempo), que desciende rápidamente hacia un nivel basal constante. Este patrón evidencia la falta de contracción voluntaria y a la actividad basal mínima del flexor carpi radialis, donde solo se registran descargas aisladas de unidades motoras o ruido de fondo.
  <p align="justify">
  Según la que se ha reportado, la amplitud esperada de la señal EMG en reposo se encuentra en el rango de 5–50 µV RMS (0.005–0.05 mV), aunque esto depende de la colocación de los electrodos y del estado de relajación muscular; sin embargo, los  valores obtenidos concuerdan con el comportamiento reportado en la literatura [11, 13]. 

- **Movimiento sin oposición:**
  ![image](https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%203%20-%20EMG/Extras/P2_SO.png?raw=true)
  <center>Figura 13: Señales EMG del flexor carpi radialis sin oposición: cruda, preprocesada y rectificada con envolvente RMS. [Elaboración propia]</center>
  <p align="justify">
  En la señal sin procesar se observa un incremento de la amplitud, alcanzando valores cercanos a ±0.45 mV. Luego de la aplicación del filtro, la señal se centra en cero, pero aun presenta las oscilaciones marcadas( -0.15 y +0.15 mV), con picos que se repiten a los largo de todo el registro. La envolvente RMS evidencia un valor promedio más elevado que en reposo (0.03 y 0.05 mV) y algunos picos que alcanzan los 0.07 mV. Este patrón corresponde a un reclutamiento intermitente de unidades motoras del flexor carpi radialis durante la flexión de la muñeca sin resistencia externa.
  <p align="justify">
  En la literatura reporta que en contracciones dinámicas voluntarias(de baja y moderada intensidad), la amplitud de la sEMG suele encontrarse en el rango de 50–300 µV RMS (0.05–0.3 mV), reflejando la suma de la actividad de varias unidades motoras activadas de forma temporal [11, 15]. Lo obtenido en la práctica de laborrito condice con los esperado para  para un músculo flexor del antebrazo en movimiento sin carga adicional, caracterizado por picos intermitentes de activación superiores a los de reposo pero sin alcanzar todavía el nivel sostenido propio de la resistencia.


- **Movimiento con oposición:**
  ![image](https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%203%20-%20EMG/Extras/P2_CO.png?raw=true)
  <center>Figura 14: Señales EMG del flexor carpi radialis con oposición: cruda, preprocesada y rectificada con envolvente RMS. [Elaboración propia]</center>
  <p align="justify">
  En esta fase se observa un gran aumento de la amplitud respecto al reposo y al movimiento libre. La señal sin procesar logra alcanzar valores de hasta ±1.2 mV, con oscilaciones continuas y de gran densidad a lo largo de la contracción. Luego de la aplicación del filtro y la eliminación del componente DC, la señal se mantiene centrada en cero y conserva amplitudes sostenidas entre -1.0 y +1.0 mV, lo que refleja la estabilidad e intensidad. La envolvente RMS muestra un ascenso progresivo hasta alcanzar valores en el rango de 0.30-0.45 mV, que se mantienen durante varios segundos antes de descender(finalización del esfuerzo). Este patrón corresponde a una contracción mantenida de alta intensidad del flexor carpi radialis, que se caracteriza por el reclutamiento masivo de unidades motoras y el aumento en la frecuencia de descarga para mantener la fuerza frente a la resistencia aplicada.
  <p align="justify">Lo que reporta la literatura es que, en contracciones intensas o máximas, los valores típicos de sEMG se sitúan en un rango de 200–1000 µV RMS (0.2–1.0 mV), aunque esto está influenciando por la carga, la fatiga y la geometría de las fibras musculares [15, 16, 17] . Lo obtenido en el laboratorio se encuentra dentro del rango reportado por la literatura. 


#### 5.3. Posición III - Dedo
- **Reposo:**
  ![image](https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%203%20-%20EMG/Extras/P3_R.png?raw=true)
  <center>Figura 15: Señales EMG del abductor pollicis brevis en reposo: cruda, preprocesada y rectificada con envolvente RMS. [Elaboración propia]</center>
  <p align="justify">
  En la señal cruda se observa una oscilación centrada en torno a 0 mV, con fluctuaciones pequeñas que no superan ±0.20 mV. Luego del preprocesamiento, la señal aún se mantiene estable en cero, con amplitudes reducidas que se encuentran en el rango de  –0.1 y +0.1 mV, lo que refleja la eliminación de artefactos de baja frecuencia y la conservación de la banda fisiológica del EMG. La envolvente RMS presenta un base baja, con valores relativamente estables en torno a 0.020 - 0.025 mV y un pico aislado cercano a 0.040 mV al final del registro(que es probable que se deba a un error al ajustar los tiempos evaluados). Este comportamiento corresponde a la actividad en reposo mínima del abductor pollicis brevis que es un músculo intrínseco de la mano en el cual la activación voluntaria está asociada a la abducción del pulgar. 
  <p align="justify">Se ha reportado, en reposo, que los músculos esqueléticos muestran amplitudes típicas en el rango de 5–50 µV RMS (0.005–0.05 mV) en EMG, que se atribuyen a descargas espontáneas de fibras musculares y al ruido del sistema de registro [11, 13]. Los valores obtenidos en el laboratorio concuerdan con dichos valores reportados en la literatura, caracterizando la condición de reposo de este músculo como una fase de baja excitabilidad eléctrica.


- **Movimiento sin oposición:**
  ![image](https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%203%20-%20EMG/Extras/P3_SO.png?raw=true)
  <center>Figura 16: Señales EMG del abductor pollicis brevis sin oposición: cruda, preprocesada y rectificada con envolvente RMS. [Elaboración propia]</center>
  <p align="justify">
  En la señal cruda se observa el incremento de la amplitud comparado a la fase de reposo, con valores que se encuentran entre -0.3 y +0.3 mV. Además, presenta rafagas intensas y frecuencias que se encuentran distribuidas de roma irregular a lo largo del registro. Luego del preprocesamiento, la señal se centra en cero y con amplitudes entre - 0.2 y +0.2 mV. La envolvente RMS muestra un nivel medio superior al reposo, con valores que oscilan entre 0.035 y 0.060 mV, y picos transitorios que alcanzan hasta 0.075 mV. Este comportamiento coincide con la activación intermitente del músculo durante la abducción voluntaria del pulgar sin resistencia, que sugiere el reclutamiento temporal de un limitado  número de unidades motoras.
  <p align="justify">Según la literatura, en contracciones dinámicas voluntarias de baja a moderada intensidad, la señal de EMG suele encontrarse en un rango de 50–300 µV RMS (0.05-0.3 mV) [11, 15]. Comparando las amplitudes obtenida en el laboratorio y lo reportado por literatura se observa que  valores de amplitud obtenidos se ubican dentro de dicho rango; sin embargo, la gran intensidad de los picos y la presencia de oscilaciones irregulares sugieren que podría existir la interferencia en los electrodos,  lo que es común en músculos pequeños de la mano por su mayor susceptibilidad a la actividad de músculos adyacentes.


- **Movimiento con oposición:**
  ![image](https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Laboratorios/Laboratorio%203%20-%20EMG/Extras/P3_CO.png?raw=true)
  <center>Figura 17: Señales EMG del abductor pollicis brevis con oposición: cruda, preprocesada y rectificada con envolvente RMS. [Elaboración propia]</center>
  <p align="justify">
  En esta fase se aprecia el incremento de la amplitud con respecto al reposo y movimiento libre. La señal cruda mantiene oscilaciones continuas y densas a lo largo de todo el registro con valores de hasta ±1.5 mV. Luego del preprocesamiento, la señal se centra en cero y su amplitud se ajusta a valores entre -0.7 a +0.8 mV. La envolvente RMS muestra valores estables alrededor de 0.20-0.30 mV, con picos que alcanzan 0.32 mV y que no regresan a la base. Este patrón corresponde a una contracción mantenida de alta intensidad del abductor pollicis brevis, en el cual se produce un reclutamiento masivo de unidades motoras y un aumento sostenido en la frecuencia de descarga para estabilizar la fuerza frente a la resistencia aplicada.
  <p align="justify">De acuerdo con la literatura, durante contracciones intensas o máximas, la amplitud de la sEMG puede situarse en un rango de 200–1000 µV RMS (0.2–1.0 mV), aunque esto se encuentra influenciado por la carga, la fatiga y la susceptibilidad a interferencias musculares en músculos pequeños de la mano [15, 16, 17]. Los valores observados se encuentran dentro de este rango de referencia; sin embargo, la gran intensidad de los picos y la presencia de oscilaciones irregulares sugieren que podría existir la interferencia en los electrodos,  lo que es común en músculos pequeños de la mano por su mayor susceptibilidad a la actividad de músculos adyacentes.

### 6.Conclusiones

<p align="justify">El análisis de las señales EEG obtenidas en el bíceps braquial, el flexor carpi radialis y el abductor pollicis brevis permitió identificar patrones diferenciados según el estado funcional del músculo. En reposo, todas las señales presentaron bajas y estables amplitudes (0.015 - 0.025 mV RMS), lo que sugiere una actividad mínima basal que es característica de las fibras musculares en ausencia de contracción voluntaria y guarda concordancia con lo que se ha reportado en la literatura para rangos típico de 5–50 µV RMS [11, 13]. Durante el movimiento libres se evidencia un aumento transitorio de la amplitud (0.025–0.045 mV RMS), que está asociando al reclutamiento intermitente y limitada de unidades motos para generar contracciones dinámicas de baja-moderada intensidad y concuerda con los valores descritos de 50–300 µV RMS [11, 15]. Finalmente, en la fase de movimiento con resistencia se registraron los mayores niveles de amplitud (0.20–0.45 mV RMS), manteniéndose  lo largo del tiempo, esto corresponde  a un reclutamiento masivo y a mayor frecuencia de descarga de las unidades motoras para mantener constante el esfuerzo,  dentro del rango de 200–1000 µV RMS que se asocia a contracciones intensas [15, 16, 17].
 
<p align="justify">Entonces, los resultados muestran un progresión clara en la activación muscular que va desde el reposo hasta la construcción con resistencia, lo que confirma la utilidad del procesamiento digital implementado (eliminación de DC, filtrado, rectificación y cálculo de la envolvente RMS) para lograr la extracción de métricas robustas de activación. Además, se constatar que la relación entre amplitud EMG y fuerza, si bien es evidente en primera instancia, puede verse afectada por factores externos como la colocación de electrodos, la presencia de artefactos de movimiento o factores internos como la interferencia de músculos adyacentes (sobretodo en los músculos más pequeños como el abductor pollicis brevis). Estos resultado refuerza la necesidad de un control cuidadoso de la adquisición y el procesamiento, así como el contraste constante con rangos bibliográficos, para lograr un interpretación convalidación de los registros de EMG en contextos experimentales. 




### :notebook:Referencias
<p align="justify">
[1] M. C. Gash, P. F. Kandle, I. V. Murray, and M. A. Varacallo, “Physiology, muscle contraction,” StatPearls - NCBI Bookshelf, Apr. 01, 2023. https://www-ncbi-nlm-nih-gov.translate.goog/sites/books/NBK537140/?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc

<p align="justify">
[2] V. Alcan and M. Zi̇Nnuroğlu, “Current developments in surface electromyography,” TURKISH JOURNAL OF MEDICAL SCIENCES, vol. 53, no. 5, pp. 1019–1031, Oct. 2023, doi: 10.55730/1300-0144.5667.

<p align="justify">
[3] F. Wang and E. M. Yiu, “Is surface electromyography (SEMG) a useful tool in identifying muscle tension dysphonia? An integrative review of the current evidence,” Journal of Voice, vol. 38, no. 3, p. 800.e1-800.e12, Dec. 2021, doi: 10.1016/j.jvoice.2021.10.006.

<p align="justify">
[4] R. E. Wagner, H. P. Da Silva, and K. Gramann, “Validation of a Low-Cost Electrocardiography (ECG) system for psychophysiological research,” Sensors, vol. 21, no. 13, p. 4485, Jun. 2021, doi: 10.3390/s21134485.

<p align="justify">
[5] “BITalino”. PLUX Biosignals. Accedido el 07 de setiembre de 2025. [En línea]. Disponible: https://www.pluxbiosignals.com/collections/bitalino?srsltid=AfmBOoqBigYX8r0j9zwN0ihDuDh8aKeExNMqrqEBD33tRp62ois9JYyd

<p align="justify">
[6] “CABLE PARA 3 ELECTRODOS – EMG/ECG – SAI SAC – MECATRONICA.”. Sisac Mecatronica. Accedido el 07 de setiembre de 2025. [En línea] https://mecatronica.saisac.pe/producto/cable-para-3-electrodos-emg-ecg-2

<p align="justify">
[7] “Batería de litio 3.7 V”. Engitronic. Accedido el 07 de setiembre de 2025. [En línea] https://www.engitronicperu.com/producto/bateria-de-litio-3-7-v

<p align="justify">
[8] “Insights that connect you to success | Opensignal”. Insights that connect you to success | Opensignal. Accedido el 26 de agosto de 2025. [En línea]. Disponible: https://www.opensignal.com/

<p align="justify">
[9] “Welcome to Python.org”. Python.org. Accedido el 26 de agosto de 2025. [En línea]. Disponible: https://www.python.org/

<p align="justify">
[10] “BITalino Lab Guides (Home Guides).”. BITalino. Accedido el 26 de agosto de 2025. [En línea]. https://support.pluxbiosignals.com/knowledge-base/bitalino-lab

<p align="justify">
[11] R. Merletti and G. L. Cerone, "Tutorial. Surface EMG detection, conditioning and pre-processing: Best practices," Journal of Electromyography and Kinesiology, vol. 54, p. 102440, Oct. 2020, doi: 10.1016/j.jelekin.2020.102440.

<p align="justify">
[12] X. Chen, Y. Zhang, and J. Zhou, "Surface Electromyography as a Natural Human-Machine Interface: A Review," IEEE Sensors Journal, vol. 22, no. 10, pp. 1–1, May 2022, doi: 10.1109/JSEN.2022.3165988.

<p align="justify">
[13] V. Gohel and N. Mehendale, "Review on electromyography signal acquisition and processing," Biophysical Reviews, vol. 12, no. 6, pp. 1361–1367, Nov. 2020, doi: 10.1007/s12551-020-00770-w.

<p align="justify">
[14] C. R. Carvalho, J. M. Fernández, A. J. del-Ama, F. O. Barroso, and J. C. Moreno, "Review of electromyography onset detection methods for real-time control of robotic exoskeletons," Journal of NeuroEngineering and Rehabilitation, vol. 20, no. 141, pp. 1–18, Oct. 2023, doi: 10.1186/s12984-023-01226-4.
<p align="justify">
[15] H. S. Milner-Brown and R. B. Stein, "The relation between the surface electromyogram and muscular force," The Journal of Physiology, vol. 246, no. 3, pp. 549–569, Apr. 1975, doi: 10.1113/jphysiol.1975.sp010904.
<p align="justify">
[16] M. Beretta-Piccoli, C. Cescon, G. D’Antona, “Evaluation of performance fatigability through surface EMG…,” Arab Journal of Basic and Applied Sciences, 28(1), 21–40, 2021. doi: 10.1080/25765299.2020.1862985 
<p align="justify">
[17] D. Simonetti, M. Hendriks, J. Herijgers, C. C. del Rio, B. Koopman, N. Keijsers, and M. Sartori, "Automated spatial localization of ankle muscle sites and model-based estimation of joint torque post-stroke via a wearable sensorised leg garment," Journal of Electromyography and Kinesiology, vol. 73, p. 102808, 2023, doi: 10.1016/j.jelekin.2023.102808.

### :raised_hand:Participación
- Eduardo Poma: 33.33%
- Rodrigo Gorbeña: 33.33%
- Jennifer Cancino: 33.33%