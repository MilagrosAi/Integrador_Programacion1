from procesador_texto import leer_archivo_texto, calcular_frecuencias_palabras, ordenar_frecuencias, mostrar_frecuencias_principales, busqueda_lineal, busqueda_hash, busqueda_binaria  # Importa funciones desde procesador_texto.py

def principal():  # Define función principal del programa
    ruta_archivo = "data/entrada.txt"  # Define ruta del archivo
    palabras = leer_archivo_texto(ruta_archivo)  # Lee archivo y obtiene palabras
    if len(palabras) == 0:  # Verifica si la lista está vacía
        print("No se encontraron palabras.")  # Imprime mensaje de error
        return  # Sale si no hay palabras
    
    print(f"Total de palabras procesadas: {len(palabras)}")  # Imprime total de palabras
    frecuencias = calcular_frecuencias_palabras(palabras)  # Calcula frecuencias
    lista_ordenada, tiempo_ordenamiento = ordenar_frecuencias(frecuencias)  # Ordena frecuencias
    print(f"Tiempo de ordenamiento rápido: {tiempo_ordenamiento:.6f} segundos")  # Imprime tiempo
    mostrar_frecuencias_principales(lista_ordenada, 10)  # Muestra 10 palabras más frecuentes
    
    ejecutando = True  # Inicializa bandera para el menú
    while ejecutando:  # Bucle para el menú
        print("\nOpciones:")  # Imprime título del menú
        print("1. Buscar una palabra")  # Opción para buscar
        print("2. Salir")  # Opción para salir
        opcion = input("Seleccione una opción (1 o 2): ")  # Lee opción del usuario
        if opcion == "1":  # Si elige buscar
            objetivo = input("Ingrese una palabra para buscar (en minúsculas, sin acentos): ")  # Pide palabra
            encontrado_lineal, tiempo_lineal = busqueda_lineal(palabras, objetivo)  # Búsqueda lineal
            encontrado_hash, tiempo_hash = busqueda_hash(frecuencias, objetivo)  # Búsqueda hash
            encontrado_binaria, tiempo_binaria = busqueda_binaria(palabras, objetivo)  # Búsqueda binaria
            print(f"\nResultados de la búsqueda de '{objetivo}':")  # Imprime título
            print(f"- Lineal: {'Encontrada' if encontrado_lineal else 'No encontrada'}, Tiempo: {tiempo_lineal:.6f} segundos")  # Resultado lineal
            print(f"- Hash: {'Encontrada' if encontrado_hash else 'No encontrada'}, Tiempo: {tiempo_hash:.6f} segundos")  # Resultado hash
            print(f"- Binaria: {'Encontrada' if encontrado_binaria else 'No encontrada'}, Tiempo: {tiempo_binaria:.6f} segundos")  # Resultado binaria
        elif opcion == "2":  # Si elige salir
            print("Saliendo del programa.")  # Imprime mensaje
            ejecutando = False  # Cambia bandera para salir
        else:  # Si opción no es válida
            print("Opción no válida, intente nuevamente.")  # Imprime error
