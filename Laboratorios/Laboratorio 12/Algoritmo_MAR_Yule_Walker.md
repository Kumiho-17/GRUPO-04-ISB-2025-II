## Modelo autoregresivo - Yule Walker
### :date:Tabla de contenidos

  - [1. Introducción](#page_facing_up1-introducción)
  - [2. Papers](#pushpin2-papers)
    - [2.1. Detección del Pico R en Señales ECG Usando Yule-Walker y Análisis de Componentes Principales](#21-detección-del-pico-r-en-señales-ecg-usando-yule-walker-y-análisis-de-componentes-principales)
    - [2.2. Modeling electrocardiogram using Yule-Walker equations and kernel machines](#22-modeling-electrocardiogram-using-yule-walker-equations-and-kernel-machines)
  - [Referencias](#notebookreferencias)
  - [Participación](#raised_handparticipación)
  
### :page_facing_up:1. Teoría breve del modelo autorregresivo (AR)
<p align="justify">
Un modelo autorregresivo (AR) es un tipo de modelo de series temporales donde la variable de interés depende linealmente de sus observaciones pasadas, es decir, el valor actual está determinado por una combinación de los valores anteriores y un término de error o ruido blanco. El modelo AR(p) se define como:

donde:
- X es el valor de la serie en el tiempo ttt,
- φi son los coeficientes autorregresivos,
- c es una constante,
- εt es el ruido blanco.


Este modelo es útil para predecir valores futuros basados en observaciones pasadas, y se usa en señales no estacionarias o con dependencia temporal. El modelo AR también es un caso especial del modelo ARMA, que incluye un componente de media móvil para modelar perturbaciones externas [1, 2].
Interpretación de un Modelo AR
Un modelo AR se puede ver como un proceso que, tras un choque o perturbación (como una sequía en la producción agrícola), afecta la variable más allá de su nivel normal, creando una desviación temporal de su equilibrio a largo plazo. Los modelos AR ayudan a predecir cómo la variable regresará a su equilibrio considerando la dependencia lineal de los valores pasados [1].
Estacionariedad y Estabilidad
Para que un modelo AR(p) sea estacionario, las raíces del polinomio característico deben estar dentro del círculo unitario, lo que garantiza que el proceso sea predecible a largo plazo [2].
Efectos de los Choques
En un modelo AR, un choque puntual afecta los valores futuros de la serie debido a la recursividad del modelo. El impacto de un choque disminuye con el tiempo en un modelo estacionario, pero su efecto persiste a través de las observaciones futuras [1].
Estimación de Coeficientes con Yule-Walker
El método Yule-Walker se usa para estimación de coeficientes AR a partir de las autocovarianzas de la serie temporal. Este método es útil para modelos de series largas y no estacionarias [2].



### :pushpin:2. Papers
#### 2.1. Detección del Pico R en Señales ECG Usando Yule-Walker y Análisis de Componentes Principales
<center><img src="https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Images/paper1.png?raw=true"/></center>
<center>Figura 1: Título del paper 1 []</center>

##### 2.1.1 Introducción 
El Electrocardiograma (ECG) es una herramienta fundamental en la medicina para la evaluación de la salud cardíaca. La detección características importantes, como el pico R, es crucial para el diagnóstico temprano de arritmias cardíacas y otros problemas del corazón. Dicho lo anterior, el artículo de Gupta y Mittal (2019) propone un enfoque combinado utilizando el modelo autoregresivo (AR) Yule-Walker y Análisis de Componentes Principales (PCA) para mejorar la detección del pico R en señales ECG [1].


##### 2.1.2 Motivación y Objetivo
<p align="justify">
El principal desafío en la detección de picos R radica en el ruido y la variabilidad en las señales ECG. Además, las grabaciones largas de ECG que son necesarias para un diagnóstico preciso requieren técnicas robustas que puedan lidiar con señales no estacionarias y ruidosas. El objetivo del estudio es:

- Mejorar la detección del pico R usando el modelo autoregresivo Yule-Walker (YW) para extraer características y PCA para mejorar la eficiencia del proceso.

- Reducir el impacto del ruido en las señales, utilizando un filtro digital pasa banda (DBPF) [1].

##### 2.1.3 Materiales y Métodos

###### 2.1.3.1 Bases de datos utilizadas

- MIT-BIH Arrhythmia Database: Base de datos clásica con 48 grabaciones de ECG a 360Hz [1].
AHA Database: Base de datos de ECG ambulatorio con 80 grabaciones [1].

- Ventricular Tachyarrhythmia (VT) Database: Contiene grabaciones de ECG de 8 minutos a 250 Hz [1].

###### 2.1.3.2 Preprocesamiento de señales

El preprocesamiento de las señales ECG se lleva a cabo en tres fases:
- Eliminación de desvío de la línea base (BLW): Para mejorar la precisión de la detección de los picos, se elimina cualquier desplazamiento no deseado en la línea base de la señal.

- Filtrado de ruido: Se aplica un filtro digital pasa banda (DBPF) con frecuencias de corte de 3 Hz (paso bajo) y 13 Hz (paso alto) para eliminar interferencias de línea de potencia y ruido muscular [1].

- Reducción de dimensiones: Se utiliza PCA para reducir la dimensionalidad de las señales, mejorando la eficiencia del proceso sin perder información importante [1].

###### 2.1.3.3 Extracción de Características Usando Yule-Walker
El modelo autoregresivo (AR) Yule-Walker es utilizado para extraer características relevantes de las señales ECG. Este modelo se basa en la representación lineal de la señal utilizando una combinación de valores pasados de la serie temporal.

###### 2.1.3.4 Funcionamiento del Modelo AR (Yule-Walker)
Un modelo AR de orden 𝑝 describe la señal Xt como una combinación lineal de sus valores pasados, más un término de error (ruido blanco):

Donde:
- Xt es el valor de la señal en el tiempo t
- φi​ son los coeficientes autorregresivos
- εt​ es el error o ruido blanco [1].


Para estimar los coeficientes φi, se utilizan las ecuaciones de Yule-Walker, que están basadas en la autocovarianza de la señal:


Donde γm​ es la autocovarianza en el retardo mmm. Las ecuaciones de Yule-Walker permiten resolver los coeficientes φi​ a partir de los valores de autocovarianza [1].

- Selección del Orden del Modelo (𝑝)

El orden 𝑝 del modelo AR es crucial. Un valor bajo de 𝑝  puede no capturar la dinámica compleja de la señal, mientras que un valor demasiado alto puede introducir sobreajuste. En este estudio, se encontró que el orden 8 proporcionaba los mejores resultados, ya que equilibraba la precisión y la complejidad del modelo [1].


##### 2.1.4 Resultados

El rendimiento de la detección del pico R fue evaluado usando varios índices de desempeño:

- Sensibilidad (SE): La proporción de picos R correctamente detectados.
- Especificidad (SP): La proporción de casos negativos correctamente identificados.
- Tasa de detección (DR): La proporción de picos R detectados en relación con los picos R reales.
- Exactitud (ACC): La precisión global del sistema.

Los resultados mostraron que el método PCA+YW obtuvo los siguientes valores de desempeño:

- Sensibilidad: 99.88%
- Especificidad: 99.92%
- Tasa de detección: 99.90%
- Exactitud: 99.81%

Estos valores superaron a los obtenidos utilizando PCA solo, que dio:

- Sensibilidad: 99.73%
- Especificidad: 99.80%
- Tasa de detección: 99.73%
- Exactitud: 99.66%

Comparando estos resultados con otros enfoques, como KNN, SVM, y Wavelet Transform, el enfoque PCA+YW mostró una mayor precisión en la detección del pico R [1].


##### 2.1.5 Discusión
###### 2.1.5.1 Interpretación de los Resultados
El método PCA+YW mostró ser altamente eficaz para la detección del pico R en señales ECG, superando a otros métodos populares debido a su alta sensibilidad y especificidad. Esto se debe a que el modelo autoregresivo Yule-Walker es capaz de capturar la dinámica temporal de la señal ECG de manera eficiente, incluso en presencia de ruido y variabilidad [1].
###### 2.1.5.2 Ventajas del método
- A diferencia de otros enfoques como KNN o SVM, el modelo AR basado en Yule-Walker es relativamente rápido y no requiere extensos procesos de entrenamiento, lo que lo hace adecuado para monitoreo en tiempo real [1].

- El uso de un filtro pasa banda digital (DBPF) en combinación con PCA y YW mejora la estabilidad del sistema, ya que puede manejar interferencias de línea de potencia y ruido muscular [1].

###### 2.1.5.2  Limitaciones y Mejoras Futuras

- Aunque el orden 𝑝 = 8 dio buenos resultados, podría haber oscilaciones para órdenes más bajos o más altos.

- Aunque este método es eficaz para la mayoría de las señales ECG, podría mejorarse para manejar mejor las señales con frecuencias más altas o más bajas [1].

##### 2.1.6 Conclusiones

El enfoque PCA+YW para la detección del pico R en señales ECG es un método eficiente y preciso que supera otras técnicas existentes en términos de sensibilidad y especificidad. Este método tiene aplicaciones prácticas en sistemas de monitorización de arritmias, marcapasos electrónicos, y sistemas de diagnóstico cardíaco. Sin embargo, en el futuro, se pueden explorar otras técnicas de extracción de características y mejoras en los algoritmos de clasificación para hacer el sistema aún más robusto y adaptable [1].



#### 2.2. Modeling electrocardiogram using Yule-Walker equations and kernel machines
<center><img src="https://github.com/Kumiho-17/GRUPO-04-ISB-2025-II/blob/master/Images/paper2.png?raw=true"/></center>
<center>Figura 2: Título del paper 2 []</center>

##### 2.2.1 Introducción 

El ECG es una señal esencial para detectar enfermedades cardíacas, pero su naturaleza no lineal dificulta su modelado con métodos lineales tradicionales como el modelo autorregresivo (AR) estimado mediante ecuaciones de Yule-Walker. Para superar esta limitación, el paper propone combinar el modelo AR con técnicas de kernel machines, que permiten transformar la señal a un espacio de alta dimensión donde el modelado lineal equivale a un modelado no lineal en el dominio original. Luego, mediante un método de pre-imagen, se recuperan predicciones interpretables en el espacio del ECG. Esta integración mejora significativamente la capacidad de representar y predecir la forma real de la señal cardíaca [2].

##### 2.2.2 Objetivo
<p align="justify">
Desarrollar un método capaz de modelar y predecir señales ECG no lineales combinando el modelo autorregresivo con técnicas kernel, aplicando ecuaciones de Yule-Walker en un espacio de características de alta dimensión y usando un método de pre-imagen para recuperar predicciones interpretables.

##### 2.2.3 Materiales y Métodos

###### 2.2.3.1 Materiales

- Señales ECG reales extraídas de MIT-BIH Normal Sinus Rhythm Database.
- 10 señales estacionarias, en ventanas de 1 minuto.
- 150 muestras por señal para entrenamiento y 150 muestras para prueba.

###### 2.2.3.2 Métodos

- Modelado AR tradicional: estimación de coeficientes AR mediante las ecuaciones de Yule-Walker, usando autocorrelación empírica.
- Extensión no lineal del AR mediante técnicas kernel: aplicación de kernel para mapear la señal a un espacio de características de alta dimensión.
- Estimación de parámetros en el espacio de características: construcción de la matriz de autocorrelación en forma de matriz kernels.
- Predicción en el espacio kernel: predicción del siguiente valor en la serie, donde la predicción queda en el espacio de alta dimensión.
- Resolución del problema de pre-imagen: aplicación de un método iterativo de punto fijo para regresar la predicción al espacio original del ECG.
- Evaluación del desempeño: comparación entre Kernel AR y AR lineal usando el error cuadrático medio (MSE) en las 150 muestras de prueba.

##### 2.2.4 Resultados

- El modelo AR lineal no logra reproducir adecuadamente el complejo QRS, mostrando una versión suavizada e imprecisa.
- El Kernel AR es capaz de seguir la forma completa del complejo QRS, manteniendo amplitud, pendiente y localización temporal.
- El modelo no lineal se adapta mejor a variaciones interpersonales en la morfología del ECG.
- El Kernel AR mantiene MSE bajo incluso en señales complejas.
- El AR lineal sufre aumentos significativos del error cuando la morfología cardíaca es más pronunciada o variable.
- En la señal 8, el error del AR lineal llega a 0.221, mientras que el Kernel AR lo reduce a 0.00039.

##### 2.2.5 Discusión

Si bien los modelos autorregresivos tradicionales ofrecen una herramienta simple para analizar series temporales, su carácter estrictamente lineal limita profundamente su capacidad para modelar la morfología del ECG, especialmente en regiones no lineales como el complejo QRS. El enfoque propuesto demuestra que esta extensión no lineal supera dichas limitaciones y permite capturar dinámicas cardíacas que el AR lineal no puede representar. Los autores subrayan que la correcta resolución del problema de pre-imagen es clave para traducir predicciones realizadas en el espacio kernel al dominio original de la señal, y aunque este paso es computacionalmente más complejo, los resultados muestran una mejora significativa en la precisión del modelado. Asimismo, se destaca que el método mantiene la simplicidad conceptual del AR, a la vez que incorpora la flexibilidad de los kernels.


##### 2.2.6 Conclusiones

Combinar el modelo autorregresivo con técnicas de kernel machines permite modelar de forma más precisa la evolución de señales ECG al capturar sus características no lineales, especialmente en zonas complejas como el QRS, donde el AR lineal falla. Al aplicar las ecuaciones de Yule-Walker, el método logra errores menores a comparación con el AR tradicional. Los resultados con señales reales del MIT-BIH confirman que esta aproximación ofrece una representación fiel a la dinámica cardíaca y una base sólida para futuras extensiones hacia modelos ARMA o ARIMA basados en kernels [2].

### :notebook:Referencias
<p align="justify">
[1] V. Gupta and M. Mittal, "R-Peak Detection in ECG Signal Using Yule-Walker and Principal Component Analysis," IETE Journal of Research, vol. 66, no. 6, pp. 921-934, 2019, doi: 10.1080/03772063.2019.1575292.

[2] R. H. Shumway and D. S. Stoffer, Time Series Analysis and Its Applications: With R Examples, 3rd ed., Springer, 2017.


### :raised_hand:Participación
- Eduardo Poma: 33.33%
- Rodrigo Gorbeña: 33.33%
- Jennifer Cancino: 33.33%