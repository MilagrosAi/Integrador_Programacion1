def ordenamiento_rapido(lista, inicio, fin, key=lambda x: x):  # Define Quick Sort con función key
    if inicio < fin:  # Verifica si rango es válido
        pivote = particion(lista, inicio, fin, key)  # Obtiene índice del pivote
        ordenamiento_rapido(lista, inicio, pivote - 1, key)  # Ordena sublista izquierda
        ordenamiento_rapido(lista, pivote + 1, fin, key)  # Ordena sublista derecha

def particion(lista, inicio, fin, key):  # Define función para particionar
    pivote = key(lista[fin])  # Elige último elemento como pivote
    i = inicio - 1  # Índice para elementos menores
    for j in range(inicio, fin):  # Itera desde inicio hasta fin-1
        if key(lista[j]) <= pivote:  # Si elemento es menor o igual
            i = i + 1  # Incrementa índice
            lista[i], lista[j] = lista[j], lista[i]  # Intercambia elementos
    lista[i + 1], lista[fin] = lista[fin], lista[i + 1]  # Coloca pivote
    return i + 1  # Devuelve índice del pivote
