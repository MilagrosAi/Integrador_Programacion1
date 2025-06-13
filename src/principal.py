from pathlib import Path  # Importa Path para manejar rutas
from procesador_texto import leer_archivo_texto, calcular_frecuencias_palabras, ordenar_frecuencias, mostrar_frecuencias_principales, busqueda_lineal, busqueda_hash, busqueda_binaria  # Importa funciones

def principal():  # Define función principal
    directorio_actual = Path(__file__).parent  # Obtiene directorio de principal.py
    ruta_archivo = directorio_actual.parent / 'data' / 'entrada.txt'  # Construye ruta absoluta
    palabras = leer_archivo_texto(str(ruta_archivo))  # Lee archivo
    if len(palabras) == 0:  # Verifica si lista está vacía
        print("Error: No se encontraron palabras en el archivo.")  # Imprime mensaje de error
        return  # Sale de la función
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
            print(f"\nResultados de la búsqueda de '{objetivo}':")  # Imprime título de resultados
            print(f"- Lineal: {'Encontrada' if encontrado_lineal else 'No encontrada'}, Tiempo: {tiempo_lineal:.6f} segundos")  # Resultado lineal
            print(f"- Hash: {'Encontrada' if encontrado_hash else 'No encontrada'}, Tiempo: {tiempo_hash:.6f} segundos")  # Resultado hash
            print(f"- Binaria: {'Encontrada' if encontrado_binaria else 'No encontrada'}, Tiempo: {tiempo_binaria:.6f} segundos")  # Resultado binaria
        elif opcion == "2":  # Si elige salir
            print("Saliendo del programa.")  # Imprime mensaje de salida
            ejecutando = False  # Cambia bandera para salir
        else:  # Si opción no válida
            print("Opción no válida, intente nuevamente.")  # Imprime mensaje de error

if __name__ == "__main__":  # Verifica si se ejecuta directamente
    principal()  # Llama a la función principal
