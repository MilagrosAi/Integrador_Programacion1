import time
from algoritmos import ordenamiento_rapido

def leer_archivo_texto(ruta_archivo):
    """Lee un archivo de texto y devuelve una lista de palabras limpias."""
    try:
        with open(ruta_archivo, 'r', encoding='latin-1') as archivo:
            texto = archivo.read().lower()
            # Dividir por espacios y eliminar puntuación
            palabras = []
            palabra_actual = ""
            for caracter in texto:
                if caracter.isalpha():
                    palabra_actual += caracter
                elif palabra_actual:
                    palabras.append(palabra_actual)
                    palabra_actual = ""
            if palabra_actual:
                palabras.append(palabra_actual)
            return [palabra for palabra in palabras if palabra]
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta_archivo}.")
        return []
    except UnicodeDecodeError:
        print(f"Error: Problema de codificación en {ruta_archivo}. Intenta con encoding='latin-1'.")
        return []

def calcular_frecuencias_palabras(palabras):
    """Calcula la frecuencia de cada palabra usando un diccionario."""
    frecuencias = {}
    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    return frecuencias

def ordenar_frecuencias(frecuencias):
    """Ordena las frecuencias usando ordenamiento rápido."""
    lista_frecuencias = [(palabra, conteo) for palabra, conteo in frecuencias.items()]
    tiempo_inicio = time.perf_counter()  # Usar perf_counter para mayor precisión
    ordenamiento_rapido(lista_frecuencias, 0, len(lista_frecuencias) - 1)
    tiempo_fin = time.perf_counter()
    return lista_frecuencias, tiempo_fin - tiempo_inicio

def busqueda_lineal(palabras, objetivo):
    """Realiza una búsqueda lineal en una lista de palabras."""
    tiempo_inicio = time.perf_counter()
    for palabra in palabras:
        if palabra == objetivo:
            tiempo_fin = time.perf_counter()
            return True, tiempo_fin - tiempo_inicio
    tiempo_fin = time.perf_counter()
    return False, tiempo_fin - tiempo_inicio

def busqueda_hash(frecuencias, objetivo):
    """Realiza una búsqueda usando un diccionario (tabla hash)."""
    tiempo_inicio = time.perf_counter()
    resultado = objetivo in frecuencias
    tiempo_fin = time.perf_counter()
    return resultado, tiempo_fin - tiempo_inicio

def mostrar_frecuencias_principales(lista_frecuencias, cantidad=5):
    """Muestra las primeras N palabras más frecuentes."""
    print(f"Las {cantidad} palabras más frecuentes:")
    for palabra, conteo in lista_frecuencias[:cantidad]:
        print(f"{palabra}: {conteo}")