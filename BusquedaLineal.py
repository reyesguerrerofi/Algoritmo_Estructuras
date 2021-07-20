import doctest
"""
Busqueda lineal
Recorre cada uno de los elementos y se compara con lo que se quiere buscar. Al final regresa todos
los indices donde aparece la busqueda.
>>> lista = [1,1,3,4,5,1,5,1,4,1,4,1]
>>> a = 1
>>> ocurrencias = []
>>> busqueda(lista,a)
[0,1,5,7,9,11]
"""

lista = [1,9,2,3,4,5,6,7,9,9,19,9,9,9,9,9]
ocurrencias = []
a = 9

def busqueda(lista,dato):
    for i in range(len(lista)):
        if lista[i] == dato:
            ocurrencias.append(i)
    return ocurrencias
    
print(busqueda(lista,a))

doctest.testmod()