from procesador_texto import leer_archivo_texto, calcular_frecuencias_palabras, ordenar_frecuencias, mostrar_frecuencias_principales, busqueda_lineal, busqueda_hash, busqueda_binaria  # Importa funciones desde procesador_texto.py

def principal():  # Define la función principal del programa
    ruta_archivo = "data/entrada.txt"  # Define la ruta del archivo de texto
    palabras = leer_archivo_texto(ruta_archivo)  # Lee el archivo y obtiene la lista de palabras
    if not palabras:  # Verifica si la lista está vacía (por error en la lectura)
        return  # Sale de la función si hay error
    
    print(f"Total de palabras procesadas: {len(palabras)}")  # Imprime el total de palabras
    frecuencias = calcular_frecuencias_palabras(palabras)  # Calcula las frecuencias de palabras
    
    lista_ordenada, tiempo_ordenamiento = ordenar_frecuencias(frecuencias)  # Ordena las frecuencias y mide el tiempo
    print(f"Tiempo de ordenamiento rápido: {tiempo_ordenamiento:.6f} segundos")  # Imprime el tiempo de Quick Sort
    mostrar_frecuencias_principales(lista_ordenada, cantidad=10)  # Muestra las 10 palabras más frecuentes
    
    while True:  # Inicia un bucle infinito para el menú
        print("\nOpciones:")  # Imprime título del menú
        print("1. Buscar una palabra")  # Opción para buscar
        print("2. Salir")  # Opción para salir
        opcion = input("Seleccione una opción (1 o 2): ")  # Lee la opción del usuario
        
        if opcion == "1":  # Si elige buscar
            objetivo = input("Ingrese una palabra para buscar (en minúsculas, sin acentos): ")  # Pide la palabra a buscar
            encontrado_lineal, tiempo_lineal = busqueda_lineal(palabras, objetivo)  # Realiza búsqueda lineal
            encontrado_hash, tiempo_hash = busqueda_hash(frecuencias, objetivo)  # Realiza búsqueda hash
            encontrado_binaria, tiempo_binaria = busqueda_binaria(palabras, objetivo)  # Realiza búsqueda binaria
            
            print(f"Búsqueda lineal: {'Encontrada' if encontrado_lineal else 'No encontrada'}, Tiempo: {tiempo_lineal:.6f} segundos")  # Imprime resultado de búsqueda lineal
            print(f"Búsqueda hash: {'Encontrada' if encontrado_hash else 'No encontrada'}, Tiempo: {tiempo_hash:.6f} segundos")  # Imprime resultado de búsqueda hash
            print(f"Búsqueda binaria: {'Encontrada' if encontrado_binaria else 'No encontrada'}, Tiempo: {tiempo_binaria:.6f} segundos")  # Imprime resultado de búsqueda binaria
        elif opcion == "2":  # Si elige salir
            print("Saliendo del programa.")  # Imprime mensaje de salida
            break  # Sale del bucle
        else:  # Si la opción no es válida
            print("Opción no válida, intente nuevamente.")  # Imprime mensaje de error

if __name__ == "__main__":  # Verifica si el archivo se ejecuta directamente
    principal()  # Llama a la función principal
