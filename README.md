Trabajo Integrador: Análisis de Archivos de Texto con Algoritmos de Búsqueda y Ordenamiento en Python
Presentación
Somos Gabriel Osvaldo Roqué y Milagros Abril Airalde, estudiantes de la Tecnicatura en Programación de la Universidad Tecnológica Nacional (UTN), cursando la asignatura Programación I en 2025. Este trabajo integrador es nuestro proyecto final para la cátedra de la profesora Cintia Rigoni.Desarrollamos un programa en Python que analiza un archivo de texto en español (data/entrada.txt), calcula la frecuencia de palabras, las ordena usando el algoritmo recursivo Quick Sort, y permite buscar palabras con búsqueda lineal, binaria, y tabla hash. El proyecto aplica conceptos de Programación I como estructuras secuenciales, condicionales, repetitivas, listas, diccionarios, funciones, y recursividad, usando codificación utf-8 para preservar ñ y acentos.
Descripción del Proyecto
El programa procesa un archivo de texto (~10,000 palabras) para:

Contar la frecuencia de palabras con un diccionario (tabla hash).
Ordenar las frecuencias con Quick Sort (O(n log n)).
Buscar palabras con:
Búsqueda lineal (O(n)).
Búsqueda binaria (O(log n)).
Búsqueda hash (O(1) promedio).


Mostrar resultados a través de un menú interactivo.

Características:

Procesa 9,831 palabras (filtrado estricto de letras, ñ, acentos, y guiones).
Usa unicodedata para normalizar caracteres y pathlib para rutas portátiles.
Mide tiempos con el módulo time:
Quick Sort: ~0.014859 segundos.
Búsqueda lineal (“horizonte”): ~0.000030 segundos.
Búsqueda hash (“horizonte”): ~0.000005 segundos.
Búsqueda binaria (“horizonte”): ~0.000010 segundos.



Estructura del Proyecto
integrador_programacion1/
├── data/
│   └── entrada.txt           # Texto en español (~10,000 palabras)
├── src/
│   ├── principal.py         # Menú e integración
│   ├── procesador_texto.py  # Lectura, frecuencias, búsquedas
│   └── algoritmos.py        # Quick Sort
│── README.md                # Este archivo
│
└──Integrador_Programacion1_Roque_Airalde_V2.pdf  # Documento

Requisitos

Python 3.11.9 (biblioteca estándar).
Sistema operativo: Windows, Linux, o macOS.
Archivo data/entrada.txt en la carpeta data/.

Instrucciones de Ejecución

Clonar el repositorio:git clone https://github.com/Ozzetas/integrador_programacion1.git

O:git clone https://github.com/MilagrosAi/Integrador_Programacion1.git


Navegar al directorio:cd integrador_programacion1


Ejecutar:python src/principal.py


Usar el menú para ver frecuencias o buscar palabras.

Resultados

Palabras procesadas: 9,831 (filtrado permite letras, ñ, acentos, guiones).
Frecuencias principales:
de: 493
las: 290
el: 290
un: 290
la: 290
en: 261
y: 261
que: 232
los: 232
es: 174


Tiempos:


Algoritmo
Palabra
Tiempo (segundos)
Complejidad



Lineal
horizonte
0.000030
O(n)


Hash
horizonte
0.000005
O(1)


Binaria
horizonte
0.000010
O(log n)


Lineal
xyz
0.000045
O(n)


Hash
xyz
0.000004
O(1)


Binaria
xyz
0.000015
O(log n)




Documentación

Documento: docs/Integrador_Programacion1_Roque_Airalde_final.docx incluye introducción, marco teórico, caso práctico, metodología, resultados, conclusiones, bibliografía, y anexos.
Video explicativo: 

Repositorios

Gabriel Roqué: https://github.com/Ozzetas/integrador_programacion1
Milagros Airalde: https://github.com/MilagrosAi/Integrador_Programacion1

Créditos

Gabriel Osvaldo Roqué: Código, documentación, pruebas.
Comision 5.
Milagros Abril Airalde: Código, documentación, pruebas.
Comision 1.
Profesor/a: Cintia Rigoni.
Asignatura: Programación I, UTN, 2025.

