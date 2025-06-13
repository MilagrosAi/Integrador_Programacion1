import time  # Importa time para medir tiempos de ejecución
import unicodedata  # Importa unicodedata para normalizar caracteres
from algoritmos import ordenamiento_rapido  # Importa Quick Sort desde algoritmos.py

def leer_archivo_texto(ruta):  # Define función para leer archivo de texto
    archivo = open(ruta, 'r', encoding='utf-8')  # Abre archivo en modo lectura con utf-8
    texto = archivo.read().lower()  # Lee texto y convierte a minúsculas
    archivo.close()  # Cierra el archivo
    texto_normalizado = unicodedata.normalize('NFC', texto)  # Normaliza a NFC para preservar ñ y acentos
    palabras = []  # Crea lista vacía para palabras
    palabra_actual = ''  # Inicializa cadena para construir palabras
    for caracter in texto_normalizado:  # Itera sobre cada carácter
        if caracter.isalpha() or caracter in 'áéíóúñ':  # Si es letra o vocal acentuada/ñ
            palabra_actual = palabra_actual + caracter  # Agrega carácter a palabra
        else:  # Si no es letra válida
            if palabra_actual:  # Si hay una palabra formada
                palabras.append(palabra_actual)  # Agrega palabra a la lista
                palabra_actual = ''  # Reinicia palabra
    if palabra_actual:  # Si queda una palabra pendiente
        palabras.append(palabra_actual)  # Agrega la última palabra
    return palabras  # Devuelve lista de palabras

def calcular_frecuencias_palabras(palabras):  # Define función para contar frecuencias
    frecuencias = {}  # Crea diccionario vacío para frecuencias
    for palabra in palabras:  # Itera sobre cada palabra
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1  # Incrementa frecuencia
    return frecuencias  # Devuelve diccionario de frecuencias

def ordenar_frecuencias(frecuencias):  # Define función para ordenar frecuencias
    lista_frecuencias = []  # Crea lista vacía para tuplas
    for palabra, freq in frecuencias.items():  # Itera sobre el diccionario
        lista_frecuencias.append((palabra, freq))  # Agrega tupla (palabra, frecuencia)
    inicio = time.perf_counter()  # Registra tiempo inicial
    ordenamiento_rapido(lista_frecuencias, 0, len(lista_frecuencias)-1, key=lambda x: x[1])  # Ordena por frecuencia
    fin = time.perf_counter()  # Registra tiempo final
    return lista_frecuencias, fin - inicio  # Devuelve lista ordenada y tiempo

def busqueda_lineal(palabras, objetivo):  # Define función para búsqueda lineal
    inicio = time.perf_counter()  # Registra tiempo inicial
    encontrado = False  # Inicializa bandera de encontrado
    tiempo = 0  # Inicializa tiempo
    for palabra in palabras:  # Itera sobre cada palabra
        if palabra == objetivo:  # Si encuentra la palabra
            fin = time.perf_counter()  # Registra tiempo final
            encontrado = True  # Marca como encontrado
            tiempo = fin - inicio  # Calcula tiempo
    if not encontrado:  # Si no se encontró
        fin = time.perf_counter()  # Registra tiempo final
        tiempo = fin - inicio  # Calcula tiempo
    return encontrado, tiempo  # Devuelve resultado y tiempo

def busqueda_hash(frecuencias, objetivo):  # Define función para búsqueda hash
    inicio = time.perf_counter()  # Registra tiempo inicial
    encontrado = objetivo in frecuencias  # Verifica si está en diccionario
    fin = time.perf_counter()  # Registra tiempo final
    tiempo = fin - inicio  # Calcula tiempo
    return encontrado, tiempo  # Devuelve resultado y tiempo

def busqueda_binaria(palabras, objetivo):  # Define función para búsqueda binaria
    palabras_ordenadas = sorted(palabras)  # Ordena lista alfabéticamente
    inicio = time.perf_counter()  # Registra tiempo inicial
    izquierda = 0  # Inicializa índice izquierdo
    derecha = len(palabras_ordenadas) - 1  # Inicializa índice derecho
    encontrado = False  # Inicializa bandera de encontrado
    while izquierda <= derecha and not encontrado:  # Mientras rango sea válido y no encontrado
        medio = (izquierda + derecha) // 2  # Calcula índice medio
        if palabras_ordenadas[medio] == objetivo:  # Si medio es el objetivo
            encontrado = True  # Marca como encontrado
        elif palabras_ordenadas[medio] < objetivo:  # Si objetivo es mayor
            izquierda = medio + 1  # Ajusta índice izquierdo
        else:  # Si objetivo es menor
            derecha = medio - 1  # Ajusta índice derecho
    fin = time.perf_counter()  # Registra tiempo final
    tiempo = fin - inicio  # Calcula tiempo
    return encontrado, tiempo  # Devuelve resultado y tiempo

def mostrar_frecuencias_principales(lista_ordenada, cantidad=10):  # Define función para mostrar frecuencias
    print("\nLas 10 palabras más frecuentes:")  # Imprime título
    indice = len(lista_ordenada) - 1  # Comienza desde el final
    contador = 0  # Contador para las palabras mostradas
    while contador < cantidad and indice >= 0:  # Mientras no se muestren todas o no se acabe la lista
        palabra, freq = lista_ordenada[indice]  # Obtiene palabra y frecuencia
        print(f"{palabra}: {freq}")  # Imprime palabra y frecuencia
        contador = contador + 1  # Incrementa contador
        indice = indice - 1  # Decrementa índice