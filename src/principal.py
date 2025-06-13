from pathlib import Path  # Importa Path para rutas
from procesador_texto import leer_archivo_texto, calcular_frecuencias_palabras, ordenar_frecuencias, mostrar_frecuencias_principales, busqueda_lineal, busqueda_hash, busqueda_binaria  # Importa funciones
print("principal.py cargado correctamente")  # Confirma carga

def principal():  # Define función principal
    print("Iniciando función principal")  # Imprime estado
    directorio_actual = Path(__file__).parent  # Obtiene directorio
    ruta_archivo = directorio_actual.parent / 'data' / 'entrada.txt'  # Construye ruta
    print(f"Ruta pathlib: {ruta_archivo}")  # Imprime ruta
    if not ruta_archivo.exists():  # Si no existe
        print("Ruta pathlib no encontrada, usando ruta manual")  # Imprime
        ruta_archivo = "data/entrada.txt"  # Ruta alternativa
        print(f"Ruta manual: {ruta_archivo}")  # Imprime
    palabras = leer_archivo_texto(str(ruta_archivo))  # Lee archivo
    print("Archivo leído, verificando palabras")  # Imprime estado
    if len(palabras) == 0:  # Si lista vacía
        print("Error: No se encontraron palabras en el archivo.")  # Imprime error
        return  # Sale
    print(f"Palabras procesadas: {len(palabras)}")  # Imprime total
    frecuencias = calcular_frecuencias_palabras(palabras)  # Calcula frecuencias
    print("Frecuencias calculadas")  # Imprime estado
    lista_ordenada, tiempo_ordenamiento = ordenar_frecuencias(frecuencias)  # Ordena
    print(f"Tiempo de ordenamiento rápido: {tiempo_ordenamiento:.6f} segundos")  # Imprime tiempo
    mostrar_frecuencias_principales(lista_ordenada, 10)  # Muestra frecuencias
    ejecutando = True  # Inicializa bandera
    while ejecutando:  # Bucle para menú
        print("\nOpciones:")  # Imprime título
        print("1. Buscar una palabra")  # Opción buscar
        print("2. Salir")  # Opción salir
        opcion = input("Seleccione una opción (1 o 2): ")  # Lee opción
        if opcion == "1":  # Si buscar
            objetivo = input("Ingrese una palabra para buscar (en minúsculas, sin acentos): ")  # Pide palabra
            encontrado_lineal, tiempo_lineal = busqueda_lineal(palabras, objetivo)  # Búsqueda lineal
            encontrado_hash, tiempo_hash = busqueda_hash(frecuencias, objetivo)  # Búsqueda hash
            encontrado_binaria, tiempo_binaria = busqueda_binaria(palabras, objetivo)  # Búsqueda binaria
            print(f"\nResultados de la búsqueda de '{objetivo}':")  # Imprime título
            print(f"- Lineal: {'Encontrada' if encontrado_lineal else 'No encontrada'}, Tiempo: {tiempo_lineal:.6f} segundos")  # Resultado
            print(f"- Hash: {'Encontrada' if encontrado_hash else 'No encontrada'}, Tiempo: {tiempo_hash:.6f} segundos")  # Resultado
            print(f"- Binaria: {'Encontrada' if encontrado_binaria else 'No encontrada'}, Tiempo: {tiempo_binaria:.6f} segundos")  # Resultado
        elif opcion == "2":  # Si salir
            print("Saliendo del programa.")  # Imprime
            ejecutando = False  # Cambia bandera
        else:  # Si inválida
            print("Opción no válida, intente nuevamente.")  # Imprime error

if __name__ == "__main__":  # Verifica ejecución directa
    print("Ejecutando programa")  # Imprime estado
    principal()  # Llama a principal

