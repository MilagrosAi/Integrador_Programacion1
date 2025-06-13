def ordenamiento_rapido(lista, inicio, fin, key=lambda x: x):  # Define Quick Sort
    if inicio < fin:  # Verifica rango
        pivote = particion(lista, inicio, fin, key)  # Obtiene pivote
        ordenamiento_rapido(lista, inicio, pivote - 1, key)  # Ordena izquierda
        ordenamiento_rapido(lista, pivote + 1, fin, key)  # Ordena derecha

def particion(lista, inicio, fin, key):  # Define partición
    pivote = key(lista[fin])  # Elige pivote
    i = inicio - 1  # Índice menores
    for j in range(inicio, fin):  # Itera
        if key(lista[j]) <= pivote:  # Si menor o igual
            i = i + 1  # Incrementa
            lista[i], lista[j] = lista[j], lista[i]  # Intercambia
    lista[i + 1], lista[fin] = lista[fin], lista[i + 1]  # Coloca pivote
    return i + 1  # Devuelve índice
