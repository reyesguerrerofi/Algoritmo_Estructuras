import doctest
"""
Ordenamiento por seleccion

>>> lista = [10,1,4,9,0,3,20]
>>> seleccion(lista)
[0,1,3,4,9,10,20]
"""

lista = [3,1,2,5,4,6,7,9,8]

def seleccion(lista):
    for i in range(len(lista)):
        minimo = min(lista[i:])
        indi = lista.index(minimo)
        aux = lista[i]
        if lista[i] > minimo:
            lista[i] = minimo
            lista[indi] = aux 
    return lista

print(seleccion(lista))

doctest.testmod()


"""
Mayor a menor
def seleccion(lista):
    for i in range(len(lista)):
        minimo = max(lista[i:])
        indi = lista.index(minimo)
        aux = lista[i]
        if lista[i] < minimo:
            lista[i] = minimo
            lista[indi] = aux 
    return lista

"""