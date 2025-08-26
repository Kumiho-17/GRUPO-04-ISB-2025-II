


### <img src="https://media.istockphoto.com/id/1150776990/es/vector/%C3%B0%C3%B0%CE%BCd-%C3%B1%C3%B01-4%C3%B1%C3%B01-2%C3%B01-2%C3%B1%C3%B0-2.jpg?s=612x612&w=0&k=20&c=Dh7C9Wj838ZBRs8nrG2MA5aOVunvb7-tmgBiNCGhVt0="  alt="Proyecto:Reconocimiento de gestos de la mano mediante señales EMG de superficie: desarrollo de un sistema accesible con fines educativos y biomédicos" width="50" height="50" style="vertical-align: middle; margin-right: 5px;" />Proyecto: Reconocimiento de gestos de la mano mediante señales EMG de superficie: desarrollo de un sistema accesible con fines educativos y biomédicos 

### 2. Introducción
<p align="justify">
Los gestos son una de las formas más naturales e intuitivas de comunicación entre las personas y su entorno, El uso de las manos, principalmente, permite expresar ideas, transmitir intención y ejecutar acciones de forma rápida y sencilla. Esta gran variedad gestual ha dado lugar a sistemas como el lenguaje de señas y, recientemente, a su aplicación en el desarrollo de interfaces naturales de usuario, donde se busca que la interacción hombre-máquina sea cada vez más fluida [1].  
En los últimos años, se han propuesto diferentes métodos para el reconocimiento de gestos. Entre ellos se encuentran los sistemas ópticos que usan cámaras para identificar el movimiento, sistemas por contracto como las pantallas táctiles y los sistemas basados en bioseñales que usa, como fuente de información, a la actividad fisiológica del usuario [1].
En esta última alternativa las señales electromiográficas (EMG) han demostrado un gran potencial. La EMG es el registro de señales eléctricas generadas por los músculos durante su movimiento. Estas señales suelen ser captadas mediante electrodos superficiales para que puedan ser procesadas y utilizadas como entradas de control en diversas aplicaciones biomédicas, como la rehabilitación o el control de prótesis mioeléctricas. Su carácter no invasivo, la portabilidad de sensores y su gran potencial de integración convierten a la EMG en una opción atrayente para aplicación de rehabilitación y el desarrollo de interfaces biomédicas. No obstante, la adquisición y procesamiento de las señales EMG presentan importantes retos como la sensibilidad al ruido, la correcta colocación de electrodos y los costos asociados a la instrumentación [2]. 

La literatura reciente muestra que la variabilidad fisiológica afecta directamente la robustez del reconocimiento de los gestos con EMG . Factores como la fatiga muscular, sudoración, el desplazamiento de los electrones y algunos cambios en la posición del brazo reducen la precisión del reconocimiento. Estudios han reportado caídas de hasta un 10% cuando un modelo entrenado en una postura es aplicado en otra diferente [3].
Aunque algunos algoritmos de deep learning pueden alcanzar precisiones de hasta el 98% estos requieren recursos elevados de cómputo [4], lo que limita su implementación en entornos educativos. 
En este escenario, investigaciones recientes han demostrado que se puede obtener resultados confiables con configuración simples y accesibles combinado con características de deep learning y de características clásicas [5]. Esto convierte al reconocimiento de gestos con EMG no solo en una tecnología prometedora, sino también en una herramienta formativa para que los estudiantes experimenten con adquisición, filtrado y clasificación de señales, reconociendo que el ruido y los artefactos son parte inherente del proceso de aprendizaje.

### 3. Problemática
<p align="justify">
El reconocimiento de gestos de la mano mediante EMG constituye una herramienta con gran futuro en campos como la rehabilitación, el control de prótesis mioeléctricas y en las interfaces hombre-máquina. Sin embargo, su implementación en ambientes prácticos enfrenta desafíos una importante brecha entre los avances de laboratorio y la realidad educativa o clínica [3, 4].
Además, aunque algunos modelos avanzados de aprendizaje profundo han alcanzado precisiones superiores al 98% en el reconocimiento de gestos [4], estos algoritmos requieren una gran capacidad de cómputo, memoria y tiempo de entrenamiento, o que restringe su uso en contextos educativos o clínicos con recursos limitados. Por otra parte, enfoques simplificados que combinan características clásicas (MAV, RMS, wavelets) con deep features han logrado resultados superiores al 90 % incluso con sistemas de un solo canal [5]. Sin embargo, todavía no se dispone de soluciones accesibles y reproducibles que permitan a los estudiantes trabajar con señales EMG en un marco didáctico.
De este modo, persiste una brecha entre el potencial demostrado de la EMG y su aprovechamiento en la formación académica. Contar con sistemas que permitan experimentar de manera clara con adquisición, filtrado y clasificación de señales resulta fundamental, reconociendo además que el ruido y los artefactos forman parte natural del aprendizaje en instrumentación biomédica.

### 4. Justificación
<p align="justify">
El desarrollo de sistemas accesibles para el reconocimiento de gestos de la mano mediante EMG resulta importante al responder a la necesidad concreta de contar con herramientas prácticas que permitan desenvolver en el entorno académico. Más allá de las limitaciones técnicas descritas en la problemática, la realización de este proyecto se basa en buscar demostrar que es posible implementar soluciones prácticas que refuercen el aprendizaje en la adquisición, filtrado y clasificación de señales, pero, además, que también siente las bases para aplicaciones futuras en rehabilitación y control prostético. 

### 5. Estado del arte
#### Ámbito comercial
- **FREEEMG.-** Dispositivo inalámbrico para el análisis de electromiografía de superficie (EMG). Su precisión en la señal, la ausencia de cables, así como el diseño ligero y compacto de sus sondas permiten evaluar cualquier tipo de movimiento en diferentes partes del cuerpo sin alterar la naturalidad del mismo. El sistema cuenta con una amplia variedad de protocolos de análisis predefinidos, que permiten evaluar la actividad muscular durante ejercicios específicos. El software procesa la información recopilada y genera automáticamente resultados gráficos, lo que facilita la comparación inmediata con valores de referencia normales [6].

![Image](https://www.btsbioengineering.com/wp-content/uploads/2022/05/05-does-not-require-dedicated-spaces.jpg)

#### Ámbito académico
- **Enhanced Hand Gesture Recognition with Surface Electromyogram and Machine Learning.-** Este estudio aborda el reconocimiento de gestos de la mano a partir de señales de electromiografía superficial (EMG) obtenidas mediante un brazalete Myo de alta precisión, empleando algoritmos de aprendizaje automático. El trabajo incluye un preprocesamiento de datos para extraer características de las señales, seguido de un conjunto de entrenamientos y pruebas. Se evaluaron cuatro modelos de machine learning en la clasificación de siete gestos distintos de los dedos, aplicando parámetros de optimización y validación de cinco pliegues. Entre los modelos analizados, el Random Forest se destacó como el más eficaz, alcanzando valores superiores al 99% en precisión, exhaustividad, F1-score y ROC-AUC. Estos resultados posicionan a Random Forest como el clasificador óptimo para el conjunto de datos EMG, con un alto potencial en aplicaciones de rehabilitación en salud y en el fortalecimiento de las tecnologías de interacción humano-computadora [7].
<img src="https://pub.mdpi-res.com/sensors/sensors-24-05231/article_deploy/html/images/sensors-24-05231-g004.png?1723536218" alt="1" style="display:inline; width:200px;"/>
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2ToqHMNp271Mp7ILZO9RzznYy0qKbwhkCyg&s" alt="2" style="display:inline; width:200px;"/>
<<<<<<< HEAD
#### Patentes
- **Gesture recognition device based on arm muscle current detection and motion sensor.-** Dispositivo de reconocimiento de gestos basado en la detección de señales eléctricas de los músculos del brazo y un sensor de movimiento. El dispositivo consiste de un anillo de mano o brazo que se coloca en la muñeca o en el antebrazo, equipado con sensores de corriente muscular. Las señales generadas durante el movimiento se procesan mediante un circuito amplificador, un filtro y un conversor analógico-digital. Posteriormente, un algoritmo de procesamiento digital en tiempo real extrae los parámetros característicos de los gestos y permite su reconocimiento. Los gestos identificados se asignan a diferentes instrucciones de control configurables, que luego se transmiten al sistema principal mediante conexión inalámbrica o cable. De esta manera, se establece un nuevo método de entrada para la interacción hombre-máquina basado en la actividad muscular del brazo [8].
=======
#### Patentes 
- **Gesture recognition device based on arm muscle current detection and motion sensor.-** Dispositivo de reconocimiento de gestos basado en la detección de señales eléctricas de los músculos del brazo y un sensor de movimiento. El dispositivo consiste de un anillo de mano o brazo que se coloca en la muñeca o en el antebrazo, equipado con sensores de corriente muscular. Las señales generadas durante el movimiento se procesan mediante un circuito amplificador, un filtro y un conversor analógico-digital. Posteriormente, un algoritmo de procesamiento digital en tiempo real extrae los parámetros característicos de los gestos y permite su reconocimiento. Los gestos identificados se asignan a diferentes instrucciones de control configurables, que luego se transmiten al sistema principal mediante conexión inalámbrica o cable. De esta manera, se establece un nuevo método de entrada para la interacción hombre-máquina basado en la actividad muscular del brazo.
>>>>>>> 31d3c80a6324f66552cdfcceaa29039229c497d5
<img src="https://patentimages.storage.googleapis.com/e5/29/ff/b0ac6a619c6c84/131102110428.png" alt="1" style="display:inline; width:200px;"/>
<img src="https://patentimages.storage.googleapis.com/8f/ac/e5/156fec5b576d4a/131102110436.png" alt="2" style="display:inline; width:200px;"/>

### 6. Objetivos
- **Objetivo general:**
<p align="justify">
Desarrollar un sistema de reconocimiento de 3 a 5 gestos de la mano a partir de señales electromiográficas (EMG), aplicando técnicas de procesamiento de señales y algoritmos de clasificación.

- **Objetivos específicos:**
    
  - Aplicar técnicas de preprocesamiento y filtrado para reducir el ruido y mejorar la calidad de las señales.
  - Extraer características relevantes en el dominio temporal y frecuencial de las señales EMG.
  - Implementar clasificadores (como KNN, SVM o redes neuronales) para el reconocimiento de gestos.
  - Evaluar el desempeño de los clasificadores utilizando métricas de precisión, sensibilidad y especificidad.

### 7. Herramientas a utilizar
- **Hardware:**
    - BITalino: dispositivo modular de adquisición biomédica que permite registrar señales fisiológicas mediante electrodos de superficie. Se usaría para capturar las señales EMG de la mano y el antebrazo, necesarias para el reconocimiento de gestos [9].
- **Software:**
    - OpenSignals: software oficial de BITalino para la adquisición y visualización en tiempo real de las señales fisiológicas. Registrará las señales EMG de los sujetos de prueba y las exportará en formatos compatibles con MATLAB o Python para su posterior análisis [10].
    - MATLAB: plataforma de programación y análisis numérico con múltiples herramientas de procesamiento de señales y machine learning. Puede filtrar las señales EMG, extraer características relevantes y entrenar modelos de clasificación de los gestos de la mano [11].
    - Python: lenguaje de programación con múltiples librerías en ciencia de datos, procesamiento de señales y aprendizaje automático. Es una alternativa a MATLAB para desarrollar los algoritmos de clasificación de gestos y validación del desempeño [12].
### 8. Referencias
[1]G. Pomboza-Junez and J. A. Holgado-Terriza, “Análisis de exactitud de reconocimiento gestual aplicando SVM y k-NN en señales EMG,” Revista Ibérica de Sistemas e Tecnologias de Informação, no. 28, pp. 15–28, Oct. 2020.  

[2]A. Suberviola Zuñiga, Control de un exoesqueleto mediante señales EMG (electromiográficas), Ph.D. dissertation, Univ. del País Vasco, 2019. [Online]. Available: http://hdl.handle.net/10810/41463 

[3]I. Kyranou, K. Szymaniak, and K. Nazarpour, “EMG Dataset for Gesture Recognition with Arm Translation,” Scientific Data, vol. 12, no. 100, 2025. [Online]. Available: https://doi.org/10.1038/s41597-024-04296-8

[4]B. Jiang, H. Wu, Q. Xia, H. Xiao, B. Peng, L. Wang, and Y. Zhao, “An efficient surface electromyography-based gesture recognition algorithm based on multiscale fusion convolution and channel attention,” Scientific Reports, vol. 14, no. 30867, 2024. [Online]. Available: https://doi.org/10.1038/s41598-024-81369-z 
<<<<<<< HEAD

[5]J. M. Fajardo, O. Gomez, and F. Prieto, “EMG hand gesture classification using handcrafted and deep features,” Biomedical Signal Processing and Control, vol. 63, p. 102210, Sep. 2020. [Online]. Available: https://doi.org/10.1016/j.bspc.2020.102210

[6] “FREEEMG | Wireless surface EMG | BTS Bioengineering”. BTS. Accedido el 26 de agosto de 2025. [En línea]. Disponible: https://www.btsbioengineering.com/products/freeemg/?gad_source=1&amp;gad_campaignid=20885113147&amp;gbraid=0AAAAAD-4nJmM2qR4mPPeKp9omYi5-MDYh&amp;gclid=CjwKCAjwtrXFBhBiEiwAEKen13qRO9cKCUIKwOSd5ppAuXZqJCIalhPxzV2pg9zgWZdNbty0WWEGVBoCdJkQAvD_BwE

[7] M. R. K. Kadavath, M. Nasor y A. Imran, “Enhanced Hand Gesture Recognition with Surface Electromyogram and Machine Learning”, Sensors, vol. 24, n.º 16, p. 5231, agosto de 2024. Accedido el 26 de agosto de 2025. [En línea]. Disponible: https://doi.org/10.3390/s24165231

[8] 不公告发明人, “Gesture recognition device based on arm muscle current detection and motion sensor”, Patente china CN103777752A, 7 de mayo de 2014.

[9] “BITalino”. PLUX Biosignals. Accedido el 26 de agosto de 2025. [En línea]. Disponible: https://www.pluxbiosignals.com/collections/bitalino?srsltid=AfmBOoqBigYX8r0j9zwN0ihDuDh8aKeExNMqrqEBD33tRp62ois9JYyd

[10] “Insights that connect you to success | Opensignal”. Insights that connect you to success | Opensignal. Accedido el 26 de agosto de 2025. [En línea]. Disponible: https://www.opensignal.com/

[11] “MATLAB - El lenguaje del cálculo técnico”. MathWorks. Accedido el 26 de agosto de 2025. [En línea]. Disponible: https://la.mathworks.com/products/matlab.html

[12] “Welcome to Python.org”. Python.org. Accedido el 26 de agosto de 2025. [En línea]. Disponible: https://www.python.org/



Participación:
Cada integrante tiene una participación de 33.3%

