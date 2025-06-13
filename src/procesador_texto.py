import time  # Importa time para medir tiempos
import unicodedata  # Importa unicodedata para normalizar
from algoritmos import ordenamiento_rapido  # Importa Quick Sort
print("procesador_texto.py cargado correctamente")  # Confirma carga del módulo

def leer_archivo_texto(ruta):  # Define función para leer archivo
    print(f"Intentando abrir archivo: {ruta}")  # Imprime ruta
    archivo = open(ruta, 'r', encoding='utf-8')  # Abre en utf-8
    texto = archivo.read().lower()  # Lee y convierte a minúsculas
    archivo.close()  # Cierra archivo
    print(f"Texto leído (primeros 50 caracteres): {texto[:50]}")  # Imprime primeros caracteres
    texto_normalizado = unicodedata.normalize('NFC', texto)  # Normaliza para ñ y acentos
    print(f"Texto normalizado (primeros 50): {texto_normalizado[:50]}")  # Imprime texto normalizado
    palabras = texto_normalizado.split()  # Divide por espacios
    print(f"Palabras iniciales: {len(palabras)}")  # Imprime cantidad
    palabras_filtradas = []  # Crea lista vacía
    for palabra in palabras:  # Itera sobre palabras
        palabra_limpia = ''  # Inicializa palabra limpia
        for caracter in palabra:  # Itera sobre caracteres
            if caracter.isalpha() or caracter in 'áéíóúñ':  # Si es letra o acento/ñ
                palabra_limpia = palabra_limpia + caracter  # Agrega
        if len(palabra_limpia) > 0:  # Si palabra no vacía
            palabras_filtradas.append(palabra_limpia)  # Agrega
    print(f"Palabras filtradas: {len(palabras_filtradas)}")  # Imprime cantidad final
    return palabras_filtradas  # Devuelve lista

def calcular_frecuencias_palabras(palabras):  # Define función para frecuencias
    print("Calculando frecuencias")  # Imprime estado
    frecuencias = {}  # Crea diccionario
    for palabra in palabras:  # Itera
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1  # Incrementa
    print(f"Frecuencias calculadas: {len(frecuencias)} palabras únicas")  # Imprime
    return frecuencias  # Devuelve diccionario

def ordenar_frecuencias(frecuencias):  # Define función para ordenar
    print("Ordenando frecuencias")  # Imprime estado
    lista_frecuencias = []  # Crea lista
    for palabra, freq in frecuencias.items():  # Itera
        lista_frecuencias.append((palabra, freq))  # Agrega tupla
    inicio = time.perf_counter()  # Registra tiempo
    ordenamiento_rapido(lista_frecuencias, 0, len(lista_frecuencias)-1, key=lambda x: x[1])  # Ordena
    fin = time.perf_counter()  # Registra tiempo
    print("Frecuencias ordenadas")  # Imprime estado
    return lista_frecuencias, fin - inicio  # Devuelve lista y tiempo

def busqueda_lineal(palabras, objetivo):  # Define búsqueda lineal
    inicio = time.perf_counter()  # Registra tiempo
    encontrado = False  # Inicializa bandera
    indice = 0  # Inicializa índice
    while indice < len(palabras) and not encontrado:  # Mientras no termine
        if palabras[indice] == objetivo:  # Si encuentra
            encontrado = True  # Marca
        indice = indice + 1  # Incrementa
    fin = time.perf_counter()  # Registra tiempo
    tiempo = fin - inicio  # Calcula tiempo
    return encontrado, tiempo  # Devuelve resultado

def busqueda_hash(frecuencias, objetivo):  # Define búsqueda hash
    inicio = time.perf_counter()  # Registra tiempo
    encontrado = objetivo in frecuencias  # Verifica
    fin = time.perf_counter()  # Registra tiempo
    tiempo = fin - inicio  # Calcula tiempo
    return encontrado, tiempo  # Devuelve resultado

def busqueda_binaria(palabras, objetivo):  # Define búsqueda binaria
    palabras_ordenadas = sorted(palabras)  # Ordena
    inicio = time.perf_counter()  # Registra tiempo
    izquierda = 0  # Inicializa izquierdo
    derecha = len(palabras_ordenadas) - 1  # Inicializa derecho
    encontrado = False  # Inicializa bandera
    while izquierda <= derecha and not encontrado:  # Mientras rango válido
        medio = (izquierda + derecha) // 2  # Calcula medio
        if palabras_ordenadas[medio] == objetivo:  # Si medio es objetivo
            encontrado = True  # Marca
        elif palabras_ordenadas[medio] < objetivo:  # Si mayor
            izquierda = medio + 1  # Ajusta
        else:  # Si menor
            derecha = medio - 1  # Ajusta
    fin = time.perf_counter()  # Registra tiempo
    tiempo = fin - inicio  # Calcula tiempo
    return encontrado, tiempo  # Devuelve resultado

def mostrar_frecuencias_principales(lista_ordenada, cantidad=10):  # Define función para mostrar
    print("\nLas 10 palabras más frecuentes:")  # Imprime título
    indice = len(lista_ordenada) - 1  # Comienza desde final
    contador = 0  # Inicializa contador
    while contador < cantidad and indice >= 0:  # Mientras no muestre todas
        palabra, freq = lista_ordenada[indice]  # Obtiene palabra y frecuencia
        print(f"{palabra}: {freq}")  # Imprime
        contador = contador + 1  # Incrementa
        indice = indice - 1  # Decrementa