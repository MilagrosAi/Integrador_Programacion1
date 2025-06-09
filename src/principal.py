# Importa funciones del módulo procesador_texto para procesar texto, calcular frecuencias y realizar búsquedas.
from procesador_texto import leer_archivo_texto, calcular_frecuencias_palabras, ordenar_frecuencias, mostrar_frecuencias_principales, busqueda_lineal, busqueda_hash

# Define la función principal que coordina el procesamiento del archivo y la interacción con el usuario.
def principal():
    # Define la ruta del archivo de texto a procesar.
    ruta_archivo = "data/entrada.txt"
    # Lee el archivo de texto y obtiene una lista de palabras normalizadas.
    palabras = leer_archivo_texto(ruta_archivo)
    # Verifica si la lista de palabras está vacía; si lo está, termina la función.
    if not palabras:
        return
    
    # Imprime el número total de palabras procesadas.
    print(f"Total de palabras procesadas: {len(palabras)}")
    # Calcula la frecuencia de cada palabra, almacenándolas en un diccionario.
    frecuencias = calcular_frecuencias_palabras(palabras)
    
    # Ordena las frecuencias en orden descendente y mide el tiempo de ordenamiento.
    lista_ordenada, tiempo_ordenamiento = ordenar_frecuencias(frecuencias)
    # Imprime el tiempo que tomó ordenar las frecuencias, con 6 decimales de precisión.
    print(f"Tiempo de ordenamiento rápido: {tiempo_ordenamiento:.6f} segundos")
    # Muestra las 10 palabras más frecuentes junto con sus frecuencias.
    mostrar_frecuencias_principales(lista_ordenada, cantidad=10)
    
    # Inicia un bucle interactivo para mostrar un menú de opciones al usuario.
    while True:
        # Imprime las opciones disponibles: buscar una palabra o salir.
        print("\nOpciones:")
        print("1. Buscar una palabra")
        print("2. Salir")
        # Solicita al usuario que seleccione una opción (1 o 2).
        opcion = input("Seleccione una opción (1 o 2): ")
        
        # Si el usuario selecciona la opción 1, realiza una búsqueda de palabra.
        if opcion == "1":
            # Solicita al usuario que ingrese la palabra a buscar, recomendando minúsculas y sin acentos.
            objetivo = input("Ingrese una palabra para buscar (en minúsculas, sin acentos si no funcionan): ")
            # Realiza una búsqueda lineal de la palabra en la lista de palabras y mide el tiempo.
            encontrado_lineal, tiempo_lineal = busqueda_lineal(palabras, objetivo)
            # Realiza una búsqueda hash de la palabra en el diccionario de frecuencias y mide el tiempo.
            encontrado_hash, tiempo_hash = busqueda_hash(frecuencias, objetivo)
            
            # Imprime el resultado de la búsqueda lineal (si se encontró o no) y el tiempo tomado.
            print(f"Búsqueda lineal: {'Encontrada' if encontrado_lineal else 'No encontrada'}, Tiempo: {tiempo_lineal:.6f} segundos")
            # Imprime el resultado de la búsqueda hash (si se encontró o no) y el tiempo tomado.
            print(f"Búsqueda hash: {'Encontrada' if encontrado_hash else 'No encontrada'}, Tiempo: {tiempo_hash:.6f} segundos")
        # Si el usuario selecciona la opción 2, termina el programa.
        elif opcion == "2":
            # Imprime un mensaje de despedida.
            print("Saliendo del programa.")
            # Sale del bucle, finalizando el programa.
            break
        # Si el usuario ingresa una opción inválida, muestra un mensaje de error.
        else:
            print("Opción no válida, intente nuevamente.")

# Verifica si el script se ejecuta directamente y, de ser así, llama a la función principal.
if __name__ == "__main__":
    principal()