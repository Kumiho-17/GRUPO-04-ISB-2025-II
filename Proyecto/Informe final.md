## <p align="center">UNIVERSIDAD PERUANA CAYETANO HEREDIA
## <p align="center">FACULTAD DE CIENCIAS E INGENIERÍA
### <p align="center">Sistema de Reconocimiento de Gestos de Mano con sEMG para la Rehabilitación Post-Accidente Cerebrovascular
<center><img src=https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Proyecto/Im%C3%A1genes/Logo.png?raw=true/></center>



Integrantes:
Eduardo Poma Soto
Jenniffer Cancino Cordero
Rodrigo Gorbeña Galarza



Docente:
Meza Rodriguez Moises Stevend




#### Resumen 
<p align="justify">
El presente trabajo desarrolla un sistema de reconocimiento de gestos de mano basado en electromiografía de superficie (sEMG) orientado a la rehabilitación de pacientes post-accidente cerebrovascular (ACV). Considerando la necesidad de herramientas objetivas y escalables para el seguimiento funcional del miembro superior —especialmente en contextos de telerehabilitación— se evaluaron tres modelos de clasificación: una CNN base, una CNN mejorada y un MLP entrenado con 110 características temporales y frecuenciales. Los resultados muestran que las CNN superan ampliamente al enfoque basado en features manuales, alcanzando la CNN mejorada una exactitud de 95.5% y separaciones más definidas entre gestos en representaciones PCA y t-SNE. Los hallazgos evidencian que la extracción automática de patrones musculares multicanal captura de manera más eficaz la fisiología del movimiento, constituyendo una alternativa robusta para el seguimiento objetivo del progreso motor en rehabilitación post-ACV.

**Palabras clave:** sEMG, rehabilitación post-ACV, reconocimiento de gestos, CNN, MLP, aprendizaje profundo, telerehabilitación, análisis de señales biomédicas.


### <p align="justify">:date: Tabla de contenidos

- [1. Introducción](#1-introducción)
- [2. Planteamiento del problema](#2-planteamiento-del-problema)
- [3. Propuesta de solución](#3-propuesta-de-solución)
- [4. Resultados](#4-resultados)
    - [4.1 Modelo 1 - CNN Base](#41-modelo-1-cnn-base)
    - [4.2 Modelo 2 - CNN Mejorada](#42-modelo-2-cnn-mejorada)
    - [4.3 Modelo 3 - MLP (110 features)](#43-modelo-3-mlp-110-features)
- [5. Conclusión](#5-conclusiones)

### <p align="justify">1. Introducción
<p align="justify">
El accidente cerebrovascular (ACV) es una interrupción súbita del flujo sanguíneo cerebral—por isquemia o hemorragia—que ocasiona déficit neurológico agudo y constituye una de las principales causas de muerte y discapacidad en el mundo. La World Stroke Organization reporta 12 millones de nuevos ACV por año y que 1 de cada 4 personas mayores de 25 años tendrá un ACV a lo largo de su vida, destacando la alta carga en años de vida ajustados por discapacidad (DALYs) incluso en población en edad productiva [1].
<p align="justify">
En Latinoamérica y el Caribe, la carga de enfermedad por ACV es elevada, con importante fracción atribuible a factores de riesgo modificables y marcada heterogeneidad regional. Un análisis específico para la región muestra que, aunque algunos países presentan menor carga relativa, el ACV sigue siendo un contribuyente mayor a mortalidad y discapacidad, con diferencias por subtipo (isquémico vs. hemorrágico) y por edad/sexo que demandan estrategias de rehabilitación costo-efectivas y escalables [2].
<p align="justify">
En Perú, el ACV se reconoce como prioridad sanitaria. El Ministerio de Salud (MINSA) aprobó la Guía técnica para el diagnóstico e inicio temprano del tratamiento de la enfermedad cerebrovascular en fase aguda a través de Telemedicina (R.M. N.° 051-2023-MINSA), con el objetivo de acelerar el acceso al manejo oportuno y estandarizado, especialmente en escenarios con limitaciones geográficas y de recursos [3]. Esta política habilita un marco para integrar estrategias de telerehabilitación durante la fase subaguda y crónica, donde la evidencia internacional muestra que, para muchos desenlaces funcionales, la telerehabilitación puede ser no inferior a la atención presencial y potencialmente más costo-efectiva cuando se implementa con canales bidireccionales clínico–paciente y protocolos adecuados [4].
<p align="justify">
En este contexto, la electromiografía de superficie (sEMG) es una herramienta clave porque cuantifica la activación muscular (amplitud, duración, patrones de reclutamiento) incluso cuando el movimiento visible aún es limitado, proporcionando biofeedback objetivo para reaprendizaje motor y medición de progreso más allá de la observación clínica subjetiva. Metaanálisis recientes en población post-ACV muestran que el biofeedback con EMG, integrado a la fisioterapia, puede mejorar la función de extremidades (p. ej., rango articular y desempeño motor), con efectos más consistentes a corto plazo y necesidad de ensayos de mayor calidad para consolidar la evidencia a largo plazo [5].
<p align="justify">
Además, la madurez del ecosistema de sensores portátiles/vestibles ha reducido barreras para el uso de sEMG en clínica y domicilio: existen plataformas comerciales y prototipos de bajo costo con metodologías de adquisición y procesamiento estandarizables, lo que facilita el seguimiento remoto, la captura de gestos de mano y la integración en esquemas de telerehabilitación centrados en la función del miembro superior [6]. Así, un proyecto de reconocimiento de gestos con EMG orientado a rehabilitación post-ACV se alinea con la necesidad de medición objetiva del progreso, con la política nacional de atención oportuna y con la evidencia que respalda modalidades remotas de cuidado [3]–[6]

### <p align="justify">2. Planteamiento del problema

<p align="justify">
El ACV es una de las principales causas de discapacidad, con alta carga de enfermedad a nivel global y regional [1]. En Perú, aunque existen lineamientos para atención oportuna (incluida telemedicina), persisten brechas en la rehabilitación del miembro superior y la evaluación sigue siendo mayormente observacional y subjetiva [2]. La sEMG permite detectar activación subclínica y ofrecer biofeedback, mostrando mejoras funcionales cuando se integra a la fisioterapia, especialmente a corto plazo [3]. Por ello, se requiere una solución accesible que use reconocimiento de gestos con sEMG para un seguimiento objetivo y escalable en telerehabilitación post-ACV [1, 3].

### <p align="justify">3. Propuesta de solución

<p align="justify">
Ante la falta de evaluaciones objetivas en la rehabilitación del miembro superior post-ACV, este estudio propone implementar un sistema de reconocimiento de gestos de mano basado en electromiografía de superficie (sEMG) orientado a seguimiento de rehabilitación post-ACV. El objetivo es cuantificar la activación muscular y ofrecer biofeedback para complementar la evaluación, especialmente en contextos de telerehabilitación. Para ello, los pacientes realizan gestos específicos del miembro superior mientras se registran señales sEMG, las cuales serán procesadas y clasificadas para identificar patrones de recuperación. Con ello se busca lograr un seguimiento preciso y continuo del progreso funcional.

### <p align="justify">4. Resultados
#### <p align="justify">4.1 Modelo 1 (CNN Base)

<p align="justify">
 El primer modelo evaluado fue una red neuronal convolucional (CNN) entrenada sobre ventanas crudas de la señal EMG previamente filtrada, rectificada y normalizada. Durante el entrenamiento, el modelo mostró una curva de aprendizaje estable con mejoría progresiva tanto en precisión como en pérdida. Tras 30 épocas de entrenamiento, el modelo alcanzó:


- <p align="justify">Exactitud en entrenamiento: ~99%
- <p align="justify">Exactitud en validación: ~85%
- <p align="justify">Exactitud en test: 86.85%

<p align="justify">
La matriz de confusión indica que el modelo logró identificar correctamente la mayoría de los cuatro gestos (G1–G4). Sin embargo, se observan confusiones entre los gestos G2 y G3, por lo que se ve solapamiento en sus patrones musculares.
El modelo sí captura información relevante, pero aún no separa completamente gestos con activaciones musculares cercanas.
<center><img src=https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Proyecto/Im%C3%A1genes/Confusi%C3%B3n%201.png?raw=true/></center>
<p align="center">Figura 1:   Matriz de Confusión de CNN Base [Fuente: Elaboración propia]
<center><img src=https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Proyecto/Im%C3%A1genes/Exactitud%20y%20p%C3%A9rdida%201.png?raw=true/></center>
<center>Figura 2:  (a) Curva de Exactitud. (b) Curva de Pérdida de CNN Base [Fuente: Elaboración propia]</center>
<center><img src=https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Proyecto/Im%C3%A1genes/PCA%20y%20t-SNE%201.png?raw=true/></center><center>Figura 3:  (a) PCA. (b) t-SNE de CNN Base [Fuente: Elaboración propia]</center>

#### <p align="justify">4.2 Modelo 2 (CNN Mejorada)

<p align="justify">
El segundo modelo corresponde a una optimización de la CNN base, incorporando técnicas para reducir el sobreajuste y mejorar la generalización. Para ello, se añadieron diferentes mecanismos durante el entrenamiento:

- <p align="justify">Detener el entrenamiento de manera automática cuando la pérdida de validación deja de mejorar durante 8 épocas, evitando aprender ruido.
- <p align="justify">Disminuir la tasa de aprendizaje en un factor de 0.5 cuando la pérdida de validación se estanca, permitiendo afinar mejor los pesos.
- <p align="justify">Evitar que la red memorice patrones específicos.

<p align="justify">
Durante el entrenamiento (50 épocas), el modelo converge antes de llegar al límite, estabilizando la pérdida en validación y ajustando la tasa de aprendizaje varias veces. En el conjunto, el modelo alcanzó:


- <p align="justify">Exactitud: 95.5%, una mejora significativa respecto a la CNN base.
- <p align="justify">Pérdida menor, indicando mejor estabilidad.
- <p align="justify">Precisión, recall y F1-score superiores en todas las clases (G1, G2, G3, G4).

<p align="justify">
La matriz de confusión mostró reducir la confusión entre gestos similares, G2 y G3, a comparación con el modelo base que presentaban mayor solapamiento.

<p align="justify">
Además, al visualizar las representaciones internas mediante PCA y t-SNE se observan agrupamientos más definidos y compactos en el espacio de 128 dimensiones. Esto confirma que el modelo mejorado logra aprender características fisiológicas más significativas, separando adecuadamente cada gesto muscular.


<center><img src=https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Proyecto/Im%C3%A1genes/Confusi%C3%B3n%202.png?raw=true/></center>
<center>Figura 4. Matriz de Confusión de CNN Mejorada [Fuente: Elaboración propia]</center>
<center><img src=https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Proyecto/Im%C3%A1genes/Exactitud%20y%20p%C3%A9rdida%202.png?raw=true/></center>
<center>Figura 5. (a) Curva de Exactitud. (b) Curva de Pérdida de CNN Mejorada [Fuente: Elaboración propia]</center>
<center><img src=https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Proyecto/Im%C3%A1genes/PCA%20y%20t-SNE%202.png?raw=true/></center><center>Figura 6. (a) PCA. (b) t-SNE de CNN Mejorada [Fuente: Elaboración propia]</center>

#### <p align="justify">4.3 Modelo 3 (MLP (110 features))

<p align="justify">
Para este último modelo se emplearon 110 features (10 canales y 11 características) extraídos por cada ventana EMG, combinando métricas temporales (MAV, RMS, WL, ZC, SSC, VAR) y frecuenciales (MNF, MDF, entropía espectral, potencias de banda, PSR). Estas características fueron escaladas para posteriormente ser utilizadas al entrenar un perceptrón multicapa con tres capas densas. El modelo obtuvo los siguientes valores en el conjunto de pruebas: Exactitud, precisión, recall, F1-score = 91%

<p align="justify">
La matriz de confusión mostró que G1 y G4 fueron las clases mejor reconocidas (precisión > 84%), G2 y G3 presentaron mayor solapamiento, por la similitud estadística en sus características EMG.

<p align="justify">
La curva de pérdida disminuye establemente sin signos de sobreajuste. La curva de exactitud alcanzó una meseta alrededor del epoch 20–25 por lo que la dimensionalidad reducida del espacio de features favorece un entrenamiento más estable respecto a los modelos basados en series temporales crudas.

<p align="justify">
El PCA mostró agrupamientos parciales pero con solapamiento entre clases, lo cual es esperable dado que la reducción lineal conserva solo ~55–60% de la varianza total.


<center><img src=https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Proyecto/Im%C3%A1genes/Confusi%C3%B3n%203.png?raw=true/></center>
<center>Figura 7. Matriz de Confusión de MLP [Fuente: Elaboración propia]</center>
<center><img src=https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Proyecto/Im%C3%A1genes/Exactitud%20y%20p%C3%A9rdida%203.png?raw=true/></center>
<center>Figura 8. (a) Curva de Exactitud. (b) Curva de Pérdida de MLP [Fuente: Elaboración propia]</center>
<center><img src=https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Proyecto/Im%C3%A1genes/PCA%20y%20t-SNE%203.png?raw=true/></center><center>Figura 9. (a) PCA. (b) t-SNE de MLP [Fuente: Elaboración propia]</center>


### <p align="justify">5. Conclusiones

- <p align="justify">El modelo 1 - CNN base tuvo un comportamiento de sobreajuste, con una exactitud alta durante el entrenamiento, pero una validación y prueba menor. Este patrón indica que la red aprendió a memorizar las características específicas del conjunto de entrenamiento en lugar de aprender patrones fisiológicos generales del EMG que sean representativos del movimiento. La ausencia de mecanismos de regularización suficientes, hizo que el modelo incrementara su complejidad efectiva, ajustándose solo a los datos vistos. Como consecuencia, cuando se evaluó con ventanas no vistas, la capacidad de generalización disminuyó, reflejando que el modelo no era robusto frente a nuevas señales, a pesar de su aparente buen rendimiento durante el entrenamiento.
- <p align="justify">Al comparar las proyecciones PCA y t-SNE entre los distintos modelos, se observaron diferencias en la representación de los gestos. En la CNN base, los embeddings muestran una agrupación parcial, pero con superposición entre los gestos G2 y G3, por lo que el modelo aprende patrones limitados y aún confunde gestos con características similares. En contraste, la CNN mejorada presenta grupos más compactos y mejor separados, esto indica que la red aprende representaciones internas más robustas y coherentes con la mejora en las métricas de clasificación. Por otro lado, en el modelo MLP, las proyecciones PCA y t-SNE muestran la mayor mezcla entre gestos, lo que sugiere que las características extraídas, no capturan la variabilidad temporal y espacial de las señales EMG.
- <p align="justify">Los resultados evidencian que los modelos basados en redes neuronales convolucionales (CNN) superan al modelo basado en características manuales (MLP con 110 features). Esto ocurre porque las CNN aprenden directamente patrones espaciales y temporales relevantes a partir de las señales EMG multicanal. A diferencia del modelo MLP que depende de descriptores previamente definidos, los cuales no capturan la fisiología del movimiento.


### <p align="justify"> Referencias

<p align="justify">[1] V. L. Feigin et al., “World Stroke Organization Global Stroke Fact Sheet 2025,” Int. J. Stroke, 2025. Disponible en: https://pmc.ncbi.nlm.nih.gov/articles/PMC11786524/
<p align="justify">[2] K. Pacheco-Barrios et al., “Burden of Stroke and Population-Attributable Fractions of Risk Factors in Latin America and the Caribbean,” J. Am. Heart Assoc., vol. 11, no. 21, e027044, 2022. DOI: 10.1161/JAHA.122.027044.
<p align="justify">[3] MINSA (Perú), “Resolución Ministerial N.° 051-2023-MINSA: Guía técnica para el diagnóstico e inicio temprano del tratamiento de las personas con enfermedad cerebrovascular en la fase aguda a través de la Telemedicina,” 2023. Disponible en: https://www.gob.pe/institucion/minsa/normas-legales/3846223-051-2023-minsa
<p align="justify">[4] NICE, Stroke rehabilitation in adults: evidence review on telerehabilitation (NG236), 2023. Disponible en: https://www.ncbi.nlm.nih.gov/books/NBK600502/bin/niceng236er14-appk-et1.pdf
<p align="justify">[5] R. Wang et al., “Electromyographic biofeedback therapy for improving limb function after stroke: A meta-analysis,” Front. Neurol., 2024. PMID: 38206927. Disponible en: https://pubmed.ncbi.nlm.nih.gov/38206927/
<p align="justify">[6] M. Al-Ayyad et al., “Electromyography Monitoring Systems in Rehabilitation: A Review of Clinical Applications, Wearable Devices and Signal Acquisition Methodologies,” Electronics, vol. 12, no. 7, 1520, 2023. DOI: 10.3390/electronics12071520. Disponible en: https://www.mdpi.com/2079-9292/12/7/1520

### Biografías de autores
E. Poma 
J. Cancino
R. Gorbeña




