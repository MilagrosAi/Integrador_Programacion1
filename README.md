Link al video de Youtube:
https://youtu.be/EFm5W9_lWmg

Análisis de Archivos de Texto con Algoritmos de Búsqueda y Ordenamiento
Este proyecto, desarrollado para la asignatura Programación I, implementa un programa en Python que analiza un archivo de texto en español para contar la frecuencia de palabras, ordenarlas usando el algoritmo Quick Sort y buscar palabras mediante búsqueda lineal y hash. El programa utiliza solo la biblioteca estándar de Python y aplica conceptos como estructuras secuenciales, condicionales, repetitivas, listas, diccionarios, recursividad y análisis de algoritmos.
Descripción
El programa lee un archivo de texto (data/entrada.txt) con 10,614 palabras, calcula las frecuencias de palabras, ordena las 10 más frecuentes con Quick Sort y permite buscar palabras a través de un menú interactivo. Los tiempos de ejecución se miden para comparar la eficiencia de los algoritmos.
Requisitos

Python 3.8 o superior.
Un archivo de texto en data/entrada.txt (incluido en el repositorio).

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

Roqué, Gabriel Osvaldo
Airalde, Milagros Abril

Licencia
Este proyecto es para fines educativos y no tiene una licencia específica.