import doctest
"""
Ejemplo burbuja

4 2 6 8 5 7
2 4 6 8 5 7
2 4 6 5 8 7
2 4 6 5 7 8
2 4 5 6 7 8

>>> listaO = [3,2,1,6,5,7,9]
>>> size = len(listaO)
>>> burbuja(listaO,size)
[1,2,3,5,6,7,9]

"""

listaO = [9,3,2,6,5,7,1]
size = len(listaO)

def burbuja(lista,size):
    for x in range(size):
        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]: 
                aux = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = aux                
    return lista

print(burbuja(listaO,size))

print(max(listaO))
print(min(listaO))
doctest.testmod()

