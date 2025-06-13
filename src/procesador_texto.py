import time  # Importa el módulo time para medir tiempos de ejecución
import unicodedata  # Importa unicodedata para normalizar caracteres con acentos
from algoritmos import ordenamiento_rapido  # Importa Quick Sort desde algoritmos.py

def leer_archivo_texto(ruta):  # Define la función para leer el archivo de texto
    try:  # Inicia un bloque try para manejar errores
        with open(ruta, 'r', encoding='utf-8') as archivo:  # Abre el archivo con codificación utf-8
            texto = archivo.read().lower()  # Lee todo el texto y lo convierte a minúsculas
            # Normaliza el texto a NFKD para separar caracteres combinados (ej., á → a + ')
            texto_normalizado = ''.join(c for c in unicodedata.normalize('NFKD', texto) 
                                      if unicodedata.category(c) != 'Mn')  # Elimina marcas diacríticas
            # Filtra solo letras y espacios, reemplazando otros caracteres por espacios
            palabras = ''.join([c if c.isalpha() or c.isspace() else ' ' for c in texto_normalizado]).split()
            return [p for p in palabras if p]  # Devuelve lista de palabras no vacías
    except FileNotFoundError:  # Captura error si el archivo no existe
        print(f"Error: El archivo {ruta} no se encontró.")  # Imprime mensaje de error
        return []  # Devuelve lista vacía
    except UnicodeDecodeError:  # Captura error de codificación
        print("Error: Problema de codificación en el archivo.")  # Imprime mensaje de error
        return []  # Devuelve lista vacía

def calcular_frecuencias_palabras(palabras):  # Define la función para contar frecuencias
    frecuencias = {}  # Crea un diccionario vacío para frecuencias
    for palabra in palabras:  # Itera sobre cada palabra
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1  # Incrementa la frecuencia
    return frecuencias  # Devuelve el diccionario de frecuencias

def ordenar_frecuencias(frecuencias):  # Define la función para ordenar frecuencias
    lista_frecuencias = [(palabra, freq) for palabra, freq in frecuencias.items()]  # Convierte diccionario a lista de tuplas
    inicio = time.perf_counter()  # Registra tiempo inicial
    ordenamiento_rapido(lista_frecuencias, 0, len(lista_frecuencias)-1, key=lambda x: x[1])  # Ordena por frecuencia
    fin = time.perf_counter()  # Registra tiempo final
    return lista_frecuencias, fin - inicio  # Devuelve lista ordenada y tiempo

def busqueda_lineal(palabras, objetivo):  # Define la función para búsqueda lineal
    inicio = time.perf_counter()  # Registra tiempo inicial
    for palabra in palabras:  # Itera sobre cada palabra
        if palabra == objetivo:  # Compara con el objetivo
            fin = time.perf_counter()  # Registra tiempo final
            return True, fin - inicio  # Devuelve True y tiempo
    fin = time.perf_counter()  # Registra tiempo final si no encuentra
    return False, fin - inicio  # Devuelve False y tiempo

def busqueda_hash(frecuencias, objetivo):  # Define la función para búsqueda hash
    inicio = time.perf_counter()  # Registra tiempo inicial
    encontrado = objetivo in frecuencias  # Verifica si está en el diccionario
    fin = time.perf_counter()  # Registra tiempo final
    return encontrado, fin - inicio  # Devuelve si se encontró y tiempo

def busqueda_binaria(palabras, objetivo):  # Define la función para búsqueda binaria
    palabras_ordenadas = sorted(palabras)  # Ordena la lista alfabéticamente
    inicio = time.perf_counter()  # Registra tiempo inicial
    izquierda, derecha = 0, len(palabras_ordenadas) - 1  # Define índices iniciales
    while izquierda <= derecha:  # Mientras el rango sea válido
        medio = (izquierda + derecha) // 2  # Calcula el índice medio
        if palabras_ordenadas[medio] == objetivo:  # Si el medio es el objetivo
            fin = time.perf_counter()  # Registra tiempo final
            return True, fin - inicio  # Devuelve True y tiempo
        elif palabras_ordenadas[medio] < objetivo:  # Si el objetivo es mayor
            izquierda = medio + 1  # Ajusta índice izquierdo
        else:  # Si el objetivo es menor
            derecha = medio - 1  # Ajusta índice derecho
    fin = time.perf_counter()  # Registra tiempo final si no encuentra
    return False, fin - inicio  # Devuelve False y tiempo

def mostrar_frecuencias_principales(lista_ordenada, cantidad=10):  # Define la función para mostrar frecuencias
    print("\nLas 10 palabras más frecuentes:")  # Imprime título
    for palabra, freq in lista_ordenada[-cantidad:][::-1]:  # Itera sobre las últimas 'cantidad' tuplas, en orden descendente
        print(f"{palabra}: {freq}")  # Imprime palabra y frecuencia