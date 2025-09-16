## :wave:Adquisición de señales ECG con BITalino
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
    - [5.1. Posición - Muñeca](#51-posición---muñeca)
  - [Referencias](#notebookreferencias)
  - [Participación](#raised_handparticipación)
  
### :page_facing_up:1. Introducción
<p align="justify">
El músculo cardíaco genera la contracción del corazón y, con ello, la acción de bombeo. El mecanismo detrás de cada contracción involucra al músculo cardíaco y a los impulsos eléctricos. 
Estos impulsos son la base de la señal registrada mediante electrocardiograma (ECG) [1].
<p align="justify">
El electrocardiograma (ECG) es empleado para registrar la actividad eléctrica cardíaca. El análisis de sus diferentes ondas permite identificar diversas alteraciones: la onda P corresponde a la despolarización auricular, el complejo QRS refleja la despolarización de los ventrículos y la onda T representa la repolarización ventricular. Cambios en estas ondas pueden señalar distintas afecciones cardíacas; por ejemplo, un complejo QRS de mayor duración a la normalidad puede sugerir un engrosamiento ventricular, característico de patologías como la hipertrofia ventricular [2].
<p align="justify">
Es así que el ECG es importante en la práctica clínica, ya que permite detectar y evaluar arritmias, enfermedades cardíacas, infartos de miocardio y otras condiciones en las que se sospechan alteraciones en la actividad eléctrica cardíaca. [3]. 
<p align="justify">
En este escenario, se vuelve necesario disponer de herramientas que posibiliten el registro, procesamiento y análisis de señales de ECG de forma práctica y confiable. Una alternativa que responde a esta necesidad es BITalino, un sistema económico y de código abierto diseñado para la adquisición de bioseñales. Este equipo integra sensores modulares y un software propio (OpenSignals), lo que permite medir señales como ECG, EMG, EEG, EDA, entre otras, resultando útil para contextos educativos y de laboratorio.[4].
<p align="justify">
En este informe se hace uso del hardware BITalino, en conjunto con su kit de herramientas y software OpenSignals, para registrar las señales ECG de un compañero de laboratorio, con el propósito de analizar e identificar los patrones eléctricos vinculados a la contracción cardíaca.

### :pushpin:2. Objetivos
- **Objetivo general:**
  <p align="justify">
  Adquirir, registrar y analizar señales biomédicas de electrocardiografía (ECG)  mediante el uso del módulo BITalino y el software OpenSignals, con el fin de comprender los principios de adquisición de bioseñales y su procesamiento básico en aplicaciones clínicas y tecnológicas.
</space>

- **Objetivos específicos:**
    
  - <p align="justify">Registrar señales biomédicas de electrocardiografía (ECG) empleando el módulo BITalino.
  - <p align="justify">Configurar el dispositivo BITalino y establecer su conexión con el software OpenSignals (r)evolution para garantizar una adquisición correcta de datos
  - <p align="justify">Obtener y exportar la información de las señales ECG desde el software, con el propósito de realizar su procesamiento y análisis posterior.

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
<center><img src="Bateria.gif" width="200" height="350"/></center> GIF "Bateria"
<center>Figura 1: Alimentación BITalino [Elaboración propia]</center>
Luego, se utilizó el canal ECG (A2) de la placa Bitalino 71-01, conectando el cable con 3 electrodos Ag/AgCl circulares como se muestra a continuación.

<center><img src="Canal.gif" width="350" height="200"/></center> GIF "Canal"
<center>Figura 2: Conexión ECG BITalino [Elaboración propia]</center>

#### 4.2. Configuración OpenSignals
Se ingresa al software OpenSignals (r)evolution.
<center><img src="Inicio.gif" width="400" height="200"/></center> GIF "Inicio"
<center>Figura 3: Ingresando a OpenSignals [Elaboración propia]</center>

<p align="justify">
Abrimos el administrador de dispositivos de Opensignals (r)evolution para acceder y configurar nuestro BITalino.

<center><img src="verde.gif" width="400" height="200"/></center> GIF "Verde"
<center>Figura 4: Administrador de dispositivos [Elaboración propia]</center>

<p align="justify">
Seleccionamos el BITalino haciendo clic en el botón ENABLED. El dispositivo estara activado si el botón ENABLED está en azul.

<center><img src="Enabled.gif" width="400" height="200"/></center> GIF "Enabled"
<center>Figura 5: Activando el BITalino [Elaboración propia]</center>

<p align="justify">
Hacemos clic en el logotipo de BITalino para acceder a su configuración. En el menú desplegable seleccionamos solo el canal ECG y deseleccionamos todos los demás. Además, configuramos su frecuencia de muestreo en 1000 Hz.

<center><img src="Confi.gif" width="400" height="200"/></center> GIF "Confi"
<center>Figura 6: Configurando el BITalino [Elaboración propia]</center>

<p align="justify">
Activamos el canal de adquisición haciendo clic en el círculo rojo (grabar).

<center><img src="Grabar.gif" width="400" height="200"/></center> GIF "Grabar"
<center>Figura 7: Adquisición de la señal [Elaboración propia]</center>

#### 4.3. Colocación de electrodos
<p align="justify">
El siguiente procedimiento consiste en colocar los electrodos ECG en el usuario. Para ello se utilizó Where should I place my Electrocardiography (ECG) electrodes? - Home Knowlegde Base BITalino [10].
Primero, retiramos la lámina protectora del electrodo antes de colocarlo en la piel.

<center><img src="Despegar.gif" width="200" height="350"/></center> GIF "Despegar"
<center>Figura 8: Retiro de lámina protectora [Elaboración propia]</center>

Colocamos el electrodo de referencia (tierra) en la cresta ilíaca.
<center><img src="Tierra.gif" width="200" height="350"/></center> GIF "Tierra"
<center>Figura 9: Electrodo de referencia [Elaboración propia]</center>

Por último, colocamos los electrodos activos sobre las muñecas.
<center><img src="Activos.gif" width="200" height="350"/></center> GIF "Activos"
<center>Figura 10: Electrodos activos [Elaboración propia]</center>

#### 4.4. Video de tomas y ploteo de OpenSignals
- Posición - Muñecas:
  Esta posición se mide desde RA (-) hasta LL (+). Teniendo la conexión de tierra en la cresta ilíaca. 
  Se tomaron las siguientes señales:
  - En reposo: 1 repetición
  - Conteniendo el aire: por 30 segundos con un descanso de 1 minuto cada repetición, tuvo 3 tomas para reducir el error.
  - Después de realizar actividad física: por 5 minutos, ejercicio aeróbico, solo tuvo una toma ya que requería más tiempo y el cansancio del usuario disminuiría en cada toma. 
  - Post-ejercicio: reposo despues de mantener la respiración.
  
  | En reposo | Manteniendo la respiración | Actividad física | Post - ejercicio |
  |-----------|----------------------------|------------------|------------------|
  | <video controls src="Reposo.mp4" title="Title"></video> Video "Reposo"| <video controls src="MR.mp4" title="Title"></video> Video "MR"| <video controls src="AF.mp4" title="Title"></video> Video "AF"| <video controls src="PE.mp4" title="Title"></video> Video "PE" |
<center>Tabla 3: Videos de la posición muñeca [Elaboración propia]</center>

### :bookmark_tabs:5. Resultados
<p align="justify">
El análisis de

#### 5.1. Posición - Muñeca
- **Reposo:**
  ![image]()
  <center>Figura 11: Señales ECG medida de la muñeca cuando se esta en reposo: cruda, preprocesada y rectificada con envolvente RMS. [Elaboración propia]</center>
  <p align="justify">
  La señal se encuentra
  <p align="justify">
  Lo que se ha reportado es que 


- **Manteniendo la respiración:**
  ![image]()
  <center>Figura 12: Señales ECG de la muñeca cuando se mantiene la respiración: cruda, preprocesada y rectificada con envolvente RMS. [Elaboración propia]</center>
  <p align="justify">
  Se nota un
  <p align="justify">
  Lo que se ha reportado es que, 

- **Actividad física:**
  ![image]()
  <center>Figura 13: Señales ECG de la muñeca cuando se reliza actividad física: cruda, preprocesada y rectificada con envolvente RMS. [Elaboración propia]</center>
  <p align="justify">
  Se aprecia un 
  <p align="justify">
  Lo que se ha reportado es que,

- **Post - ejercicio:**
  ![image]()
  <center>Figura 13: Señales ECG de la muñeca cuando se reliza actividad física: cruda, preprocesada y rectificada con envolvente RMS. [Elaboración propia]</center>
  <p align="justify">
  Se aprecia un 
  <p align="justify">
  Lo que se ha reportado es que,

### :notebook:Referencias
<p align="justify">
[1] R. Ripa, T. George, K. R. Shumway, and Y. Sattar, “Physiology, cardiac muscle,” StatPearls - NCBI Bookshelf, Jul. 30, 2023. https://www.ncbi.nlm.nih.gov/books/NBK572070

<p align="justify">
[2] Y. Sattar and L. Chhabra, “Electrocardiogram,” StatPearls - NCBI Bookshelf, Jun. 05, 2023. https://www.ncbi.nlm.nih.gov/books/NBK549803/

<p align="justify">
[3] K. B. Hudson, A. Sudhir, G. F. Glass, and W. Brady, The electrocardiogram in emergency and acute care. Wiley-Blackwell, 2022.

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
[10] “Where should I place my Electrocardiography (ECG) electrodes?”. BITalino. Accedido el 10 de setiembre de 2025. [En línea]. Disponible: https://support.pluxbiosignals.com/knowledge-base/where-should-i-place-my-electrocardiocraphy-ecg-electrodes

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