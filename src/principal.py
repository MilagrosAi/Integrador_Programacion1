from procesador_texto import leer_archivo_texto, calcular_frecuencias_palabras, ordenar_frecuencias, mostrar_frecuencias_principales, busqueda_lineal, busqueda_hash

def principal():
    ruta_archivo = "data/entrada.txt"
    palabras = leer_archivo_texto(ruta_archivo)
    if not palabras:
        return
    
    print(f"Total de palabras procesadas: {len(palabras)}")
    frecuencias = calcular_frecuencias_palabras(palabras)
    
    lista_ordenada, tiempo_ordenamiento = ordenar_frecuencias(frecuencias)
    print(f"Tiempo de ordenamiento rápido: {tiempo_ordenamiento:.6f} segundos")
    mostrar_frecuencias_principales(lista_ordenada, cantidad=10)
    
    while True:
        print("\nOpciones:")
        print("1. Buscar una palabra")
        print("2. Salir")
        opcion = input("Seleccione una opción (1 o 2): ")
        
        if opcion == "1":
            objetivo = input("Ingrese una palabra para buscar (en minúsculas, sin acentos si no funcionan): ")
            encontrado_lineal, tiempo_lineal = busqueda_lineal(palabras, objetivo)
            encontrado_hash, tiempo_hash = busqueda_hash(frecuencias, objetivo)
            
            print(f"Búsqueda lineal: {'Encontrada' if encontrado_lineal else 'No encontrada'}, Tiempo: {tiempo_lineal:.6f} segundos")
            print(f"Búsqueda hash: {'Encontrada' if encontrado_hash else 'No encontrada'}, Tiempo: {tiempo_hash:.6f} segundos")
        elif opcion == "2":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    principal()