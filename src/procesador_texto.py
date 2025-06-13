# Importa el módulo time para medir tiempos de ejecución.
import time
# Importa la función ordenamiento_rapido desde el módulo algoritmos.
from algoritmos import ordenamiento_rapido

# Define una función para leer un archivo de texto y extraer palabras normalizadas.
def leer_archivo_texto(ruta_archivo):
    """Lee un archivo de texto y devuelve una lista de palabras limpias."""
    # Intenta abrir y procesar el archivo.
    try:
        # Abre el archivo en modo lectura con codificación 'latin-1'.
        with open(ruta_archivo, 'r', encoding='latin-1') as archivo:
            # Lee todo el contenido del archivo y lo convierte a minúsculas.
            texto = archivo.read().lower()
            # Inicializa una lista para almacenar las palabras.
            palabras = []
            # Inicializa una cadena para construir cada palabra.
            palabra_actual = ""
            # Itera sobre cada carácter del texto.
            for caracter in texto:
                # Si el carácter es una letra, lo agrega a la palabra actual.
                if caracter.isalpha():
                    palabra_actual += caracter
                # Si no es una letra y hay una palabra acumulada, la guarda.
                elif palabra_actual:
                    palabras.append(palabra_actual)
                    palabra_actual = ""
            # Agrega la última palabra acumulada, si existe.
            if palabra_actual:
                palabras.append(palabra_actual)
            # Filtra palabras vacías y devuelve la lista de palabras.
            return [palabra for palabra in palabras if palabra]
    # Maneja el error si el archivo no se encuentra.
    except FileNotFoundError:
        # Imprime un mensaje de error y devuelve una lista vacía.
        print(f"Error: No se encontró el archivo {ruta_archivo}.")
        return []
    # Maneja el error si hay problemas de codificación.
    except UnicodeDecodeError:
        # Imprime un mensaje de error sugiriendo la codificación 'latin-1' y devuelve una lista vacía.
        print(f"Error: Problema de codificación en {ruta_archivo}. Intenta con encoding='latin-1'.")
        return []

# Define una función para contar la frecuencia de cada palabra.
def calcular_frecuencias_palabras(palabras):
    """Calcula la frecuencia de cada palabra usando un diccionario."""
    # Inicializa un diccionario para almacenar las frecuencias.
    frecuencias = {}
    # Itera sobre cada palabra en la lista.
    for palabra in palabras:
        # Si la palabra ya está en el diccionario, incrementa su contador.
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        # Si es una palabra nueva, la agrega con un contador inicial de 1.
        else:
            frecuencias[palabra] = 1
    # Devuelve el diccionario de frecuencias.
    return frecuencias

# Define una función para ordenar las frecuencias de palabras.
def ordenar_frecuencias(frecuencias):
    """Ordena las frecuencias usando ordenamiento rápido."""
    # Convierte el diccionario de frecuencias en una lista de tuplas (palabra, conteo).
    lista_frecuencias = [(palabra, conteo) for palabra, conteo in frecuencias.items()]
    # Registra el tiempo inicial para medir el ordenamiento.
    tiempo_inicio = time.perf_counter()  # Usar perf_counter para mayor precisión
    # Llama a la función de ordenamiento rápido para ordenar la lista.
    ordenamiento_rapido(lista_frecuencias, 0, len(lista_frecuencias) - 1)
    # Registra el tiempo final tras el ordenamiento.
    tiempo_fin = time.perf_counter()
    # Devuelve la lista ordenada y el tiempo total de ordenamiento.
    return lista_frecuencias, tiempo_fin - tiempo_inicio

# Define una función para buscar una palabra en la lista usando búsqueda lineal.
def busqueda_lineal(palabras, objetivo):
    """Realiza una búsqueda lineal en una lista de palabras."""
    # Registra el tiempo inicial para medir la búsqueda.
    tiempo_inicio = time.perf_counter()
    # Itera sobre cada palabra en la lista.
    for palabra in palabras:
        # Si encuentra la palabra objetivo, registra el tiempo final y devuelve True.
        if palabra == objetivo:
            tiempo_fin = time.perf_counter()
            return True, tiempo_fin - tiempo_inicio
    # Si no encuentra la palabra, registra el tiempo final y devuelve False.
    tiempo_fin = time.perf_counter()
    return False, tiempo_fin - tiempo_inicio

# Define una función para buscar una palabra usando un diccionario (tabla hash).
def busqueda_hash(frecuencias, objetivo):
    """Realiza una búsqueda usando un diccionario (tabla hash)."""
    # Registra el tiempo inicial para medir la búsqueda.
    tiempo_inicio = time.perf_counter()
    # Verifica si la palabra objetivo está en el diccionario de frecuencias.
    resultado = objetivo in frecuencias
    # Registra el tiempo final tras la búsqueda.
    tiempo_fin = time.perf_counter()
    # Devuelve el resultado de la búsqueda (True/False) y el tiempo total.
    return resultado, tiempo_fin - tiempo_inicio

def busqueda_binaria(palabras, objetivo):  # Define la nueva función para búsqueda binaria
    palabras_ordenadas = sorted(palabras)  # Ordena la lista de palabras alfabéticamente
    inicio = time.perf_counter()  # Registra el tiempo inicial
    izquierda, derecha = 0, len(palabras_ordenadas) - 1  # Define los índices iniciales
    while izquierda <= derecha:  # Mientras el rango de búsqueda sea válido
        medio = (izquierda + derecha) // 2  # Calcula el índice medio
        if palabras_ordenadas[medio] == objetivo:  # Si el elemento medio es el objetivo
            fin = time.perf_counter()  # Registra el tiempo final
            return True, fin - inicio  # Devuelve True y el tiempo
        elif palabras_ordenadas[medio] < objetivo:  # Si el objetivo es mayor
            izquierda = medio + 1  # Ajusta el índice izquierdo
        else:  # Si el objetivo es menor
            derecha = medio - 1  # Ajusta el índice derecho
    fin = time.perf_counter()  # Registra el tiempo final si no se encuentra
    return False, fin - inicio  # Devuelve False y el tiempo

# Define una función para mostrar las palabras más frecuentes.
def mostrar_frecuencias_principales(lista_frecuencias, cantidad=5):
    """Muestra las primeras N palabras más frecuentes."""
    # Imprime un encabezado indicando cuántas palabras se mostrarán.
    print(f"Las {cantidad} palabras más frecuentes:")
    # Itera sobre las primeras 'cantidad' tuplas de la lista de frecuencias.
    for palabra, conteo in lista_frecuencias[:cantidad]:
        # Imprime cada palabra y su frecuencia.
        print(f"{palabra}: {conteo}")