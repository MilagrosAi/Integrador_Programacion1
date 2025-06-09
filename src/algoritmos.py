def ordenamiento_rapido(lista, comienzo, fin):
    """Ordena una lista de tuplas (palabra, frecuencia) por frecuencia de forma recursiva."""
    if comienzo < fin:
        indice_pivote = particion(lista, comienzo, fin)
        ordenamiento_rapido(lista, comienzo, indice_pivote - 1)
        ordenamiento_rapido(lista, indice_pivote + 1, fin)

def particion(lista, comienzo, fin):
    """Particiona la lista usando el último elemento como pivote."""
    pivote = lista[fin][1]  # Frecuencia del último elemento
    i = comienzo - 1
    for j in range(comienzo, fin):
        if lista[j][1] >= pivote:  # Orden descendente por frecuencia
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    lista[i + 1], lista[fin] = lista[fin], lista[i + 1]
    return i + 1