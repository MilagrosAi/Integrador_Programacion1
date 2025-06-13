import time  # Importa time para medir tiempos
import unicodedata  # Importa unicodedata para normalizar caracteres
from algoritmos import ordenamiento_rapido  # Importa Quick Sort

def leer_archivo_texto(ruta):  # Define función para leer archivo
    archivo = open(ruta, 'r', encoding='utf-8')  # Abre archivo en utf-8
    texto = archivo.read().lower()  # Lee texto y convierte a minúsculas
    archivo.close()  # Cierra archivo
    texto_normalizado = unicodedata.normalize('NFC', texto)  # Normaliza para ñ y acentos
    palabras = texto_normalizado.split()  # Divide por espacios
    palabras_filtradas = []  # Crea lista vacía para palabras filtradas
    for palabra in palabras:  # Itera sobre palabras iniciales
        palabra_limpia = ''  # Inicializa palabra limpia
        for caracter in palabra:  # Itera sobre caracteres
            if caracter.isalpha() or caracter in 'áéíóúñ-':  # Si es letra, acento, ñ o guion
                palabra_limpia = palabra_limpia + caracter  # Agrega a palabra limpia
        if len(palabra_limpia) > 0:  # Si palabra no vacía
            palabras_filtradas.append(palabra_limpia)  # Agrega a lista filtrada
    return palabras_filtradas  # Devuelve lista de palabras

def calcular_frecuencias_palabras(palabras):  # Define función para contar frecuencias
    frecuencias = {}  # Crea diccionario vacío
    for palabra in palabras:  # Itera sobre palabras
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1  # Incrementa frecuencia
    return frecuencias  # Devuelve diccionario de frecuencias

def ordenar_frecuencias(frecuencias):  # Define función para ordenar frecuencias
    lista_frecuencias = []  # Crea lista vacía
    for palabra, freq in frecuencias.items():  # Itera sobre diccionario
        lista_frecuencias.append((palabra, freq))  # Agrega tupla (palabra, frecuencia)
    inicio = time.perf_counter()  # Registra tiempo inicial
    ordenamiento_rapido(lista_frecuencias, 0, len(lista_frecuencias)-1, key=lambda x: x[1])  # Ordena por frecuencia
    fin = time.perf_counter()  # Registra tiempo final
    return lista_frecuencias, fin - inicio  # Devuelve lista ordenada y tiempo

def busqueda_lineal(palabras, objetivo):  # Define búsqueda lineal
    inicio = time.perf_counter()  # Registra tiempo inicial
    encontrado = False  # Inicializa bandera de encontrado
    indice = 0  # Inicializa índice
    while indice < len(palabras) and not encontrado:  # Mientras no termine lista
        if palabras[indice] == objetivo:  # Si encuentra palabra
            encontrado = True  # Marca como encontrado
        indice = indice + 1  # Incrementa índice
    fin = time.perf_counter()  # Registra tiempo final
    tiempo = fin - inicio  # Calcula tiempo
    return encontrado, tiempo  # Devuelve resultado y tiempo

def busqueda_hash(frecuencias, objetivo):  # Define búsqueda hash
    inicio = time.perf_counter()  # Registra tiempo inicial
    encontrado = objetivo in frecuencias  # Verifica si está en diccionario
    fin = time.perf_counter()  # Registra tiempo final
    tiempo = fin - inicio  # Calcula tiempo
    return encontrado, tiempo  # Devuelve resultado y tiempo

def busqueda_binaria(palabras, objetivo):  # Define búsqueda binaria
    palabras_ordenadas = sorted(palabras)  # Ordena lista alfabéticamente
    inicio = time.perf_counter()  # Registra tiempo inicial
    izquierda = 0  # Inicializa índice izquierdo
    derecha = len(palabras_ordenadas) - 1  # Inicializa índice derecho
    encontrado = False  # Inicializa bandera
    while izquierda <= derecha and not encontrado:  # Mientras rango válido
        medio = (izquierda + derecha) // 2  # Calcula índice medio
        if palabras_ordenadas[medio] == objetivo:  # Si medio es objetivo
            encontrado = True  # Marca como encontrado
        elif palabras_ordenadas[medio] < objetivo:  # Si objetivo mayor
            izquierda = medio + 1  # Ajusta izquierdo
        else:  # Si objetivo menor
            derecha = medio - 1  # Ajusta derecho
    fin = time.perf_counter()  # Registra tiempo final
    tiempo = fin - inicio  # Calcula tiempo
    return encontrado, tiempo  # Devuelve resultado y tiempo

def mostrar_frecuencias_principales(lista_ordenada, cantidad=10):  # Define función para mostrar
    print("\nLas 10 palabras más frecuentes:")  # Imprime título
    indice = len(lista_ordenada) - 1  # Comienza desde el final
    contador = 0  # Inicializa contador
    while contador < cantidad and indice >= 0:  # Mientras no muestre todas
        palabra, freq = lista_ordenada[indice]  # Obtiene palabra y frecuencia
        print(f"{palabra}: {freq}")  # Imprime palabra y frecuencia
        contador = contador + 1  # Incrementa contador
        indice = indice - 1  # Decrementa índice