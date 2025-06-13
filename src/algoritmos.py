def ordenamiento_rapido(lista, inicio, fin, key=lambda x: x):  # Define Quick Sort con una función key para ordenar
    if inicio < fin:  # Verifica si el rango es válido
        pivote = particion(lista, inicio, fin, key)  # Obtiene el índice del pivote
        ordenamiento_rapido(lista, inicio, pivote - 1, key)  # Ordena la sublista izquierda
        ordenamiento_rapido(lista, pivote + 1, fin, key)  # Ordena la sublista derecha

def particion(lista, inicio, fin, key):  # Define la función para particionar la lista
    pivote = key(lista[fin])  # Elige el último elemento como pivote
    i = inicio - 1  # Índice para elementos menores que el pivote
    for j in range(inicio, fin):  # Itera desde inicio hasta fin-1
        if key(lista[j]) <= pivote:  # Si el elemento es menor o igual al pivote
            i += 1  # Incrementa el índice de menores
            lista[i], lista[j] = lista[j], lista[i]  # Intercambia elementos
    lista[i + 1], lista[fin] = lista[fin], lista[i + 1]  # Coloca el pivote en su posición final
    return i + 1  # Devuelve el índice del pivote
