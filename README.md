Análisis de Archivos de Texto con Algoritmos de Búsqueda y Ordenamiento
Este proyecto, desarrollado para la asignatura Programación I, implementa un programa en Python que analiza un archivo de texto en español para contar la frecuencia de palabras, ordenarlas usando el algoritmo Quick Sort y buscar palabras mediante búsqueda lineal y hash. El programa utiliza solo la biblioteca estándar de Python y aplica conceptos como estructuras secuenciales, condicionales, repetitivas, listas, diccionarios, recursividad y análisis de algoritmos.
Descripción
El programa lee un archivo de texto (data/entrada.txt) con 10,614 palabras, calcula las frecuencias de palabras, ordena las 10 más frecuentes con Quick Sort y permite buscar palabras a través de un menú interactivo. Los tiempos de ejecución se miden para comparar la eficiencia de los algoritmos.
Requisitos

Python 3.8 o superior.
Un archivo de texto en data/entrada.txt (incluido en el repositorio).

Instalación

Clona el repositorio:git clone https://github.com/Ozzetas/integrador_programacion1.git


Navega al directorio del proyecto:cd integrador_programacion1


Asegúrate de estar en la rama master:git checkout master


Asegúrate de que el archivo data/entrada.txt esté presente.

Uso

Ejecuta el programa principal:python src/principal.py


El programa mostrará:
Total de palabras procesadas (10,614).
Las 10 palabras más frecuentes (por ejemplo, “de: 493”, “a: 348”).
Un menú interactivo para buscar palabras o salir.


Sigue las instrucciones del menú para buscar palabras (en minúsculas, sin acentos si es necesario).

Estructura del Proyecto

src/
principal.py: Integra los módulos y ejecuta el programa con un menú interactivo.
procesador_texto.py: Maneja la lectura del archivo, cálculo de frecuencias y búsquedas.
algoritmos.py: Implementa el algoritmo Quick Sort.


data/
entrada.txt: Archivo de texto en español con 10,614 palabras.


README.md: Este archivo.

Resultados

Total de palabras: 10,614.
Palabras más frecuentes:
de: 493
a: 348
el: 290
la: 290
un: 290
las: 290
en: 261
y: 261
que: 232
los: 232


Tiempo de Quick Sort: ~0.002849 segundos.
Tiempos de búsqueda (ejemplo con “horizonte”):
Búsqueda lineal: ~0.000030 segundos.
Búsqueda hash: ~0.000005 segundos.



Autores

Ozzetas
[Nombre de tu compañera]

Licencia
Este proyecto es para fines educativos y no tiene una licencia específica.
