import time  # Importa time para medir tiempos
import unicodedata  # Importa unicodedata para normalizar caracteres
from algoritmos import ordenamiento_rapido  # Importa Quick Sort

def leer_archivo_texto(ruta):  # Define función para leer archivo
    archivo = open(ruta, 'r', encoding='utf-8')  # Abre archivo en utf-8
    texto = archivo.read().lower()  # Lee texto y convierte a minúsculas
    archivo.close()  # Cierra archivo
    print(f"Primeros 100 caracteres: {texto[:100]}")  # Imprime primeros 100 caracteres para depuración
    texto_normalizado = unicodedata.normalize('NFC', texto)  # Normaliza a NFC para ñ y acentos
    palabras = []  # Crea lista vacía
    palabra_actual = ''  # Inicializa cadena
    for caracter in texto_normalizado:  # Itera sobre caracteres
        if caracter.isalpha() or caracter in 'áéíóúñ':  # Si es letra o acento/ñ
            palabra_actual = palabra_actual + caracter  # Agrega a palabra
        else:  # Si no es letra válida
            if len(palabra_actual) > 0:  # Si hay palabra formada
                palabras.append(palabra_actual)  # Agrega a lista
                palabra_actual = ''  # Reinicia palabra
    if len(palabra_actual) > 0:  # Si queda palabra
        palabras.append(palabra_actual)  # Agrega última palabra
    print(f"Palabras encontradas: {len(palabras)}")  # Imprime cantidad de palabras
    return palabras  # Devuelve lista

def calcular_frecuencias_palabras(palabras):  # Define función para contar frecuencias
    frecuencias = {}  # Crea diccionario vacío
    for palabra in palabras:  # Itera sobre palabras
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1  # Incrementa frecuencia
    return frecuencias  # Devuelve diccionario

def ordenar_frecuencias(frecuencias):  # Define función para ordenar
    lista_frecuencias = []  # Crea lista vacía
    for palabra, freq in frecuencias.items():  # Itera sobre diccionario
        lista_frecuencias.append((palabra, freq))  # Agrega tupla
    inicio = time.perf_counter()  # Registra tiempo inicial
    ordenamiento_rapido(lista_frecuencias, 0, len(lista_frecuencias)-1, key=lambda x: x[1])  # Ordena
    fin = time.perf_counter()  # Registra tiempo final
    return lista_frecuencias, fin - inicio  # Devuelve lista y tiempo

def busqueda_lineal(palabras, objetivo):  # Define búsqueda lineal
    inicio = time.perf_counter()  # Registra tiempo inicial
    encontrado = False  # Inicializa bandera
    indice = 0  # Inicializa índice
    while indice < len(palabras) and not encontrado:  # Mientras no termine lista
        if palabras[indice] == objetivo:  # Si encuentra palabra
            encontrado = True  # Marca encontrado
        indice = indice + 1  # Incrementa índice
    fin = time.perf_counter()  # Registra tiempo final
    tiempo = fin - inicio  # Calcula tiempo
    return encontrado, tiempo  # Devuelve resultado y tiempo

def busqueda_hash(frecuencias, objetivo):  # Define búsqueda hash
    inicio = time.perf_counter()  # Registra tiempo inicial
    encontrado = objetivo in frecuencias  # Verifica en diccionario
    fin = time.perf_counter()  # Registra tiempo final
    tiempo = fin - inicio  # Calcula tiempo
    return encontrado, tiempo  # Devuelve resultado y tiempo

def busqueda_binaria(palabras, objetivo):  # Define búsqueda binaria
    palabras_ordenadas = sorted(palabras)  # Ordena alfabéticamente
    inicio = time.perf_counter()  # Registra tiempo inicial
    izquierda = 0  # Inicializa índice izquierdo
    derecha = len(palabras_ordenadas) - 1  # Inicializa índice derecho
    encontrado = False  # Inicializa bandera
    while izquierda <= derecha and not encontrado:  # Mientras rango válido
        medio = (izquierda + derecha) // 2  # Calcula medio
        if palabras_ordenadas[medio] == objetivo:  # Si medio es objetivo
            encontrado = True  # Marca encontrado
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
        print(f"{palabra}: {freq}")  # Imprime
        contador = contador + 1  # Incrementa contador
        indice = indice - 1  # Decrementa índice
        