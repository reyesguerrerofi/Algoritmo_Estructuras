"""
Busqueda Binaria
Requisitos: Tener la lista ordenada de manera ascendente (menor a mayor). No valores repetidos

"""

lista = [1,9,4,2,5,6,7,10]

def ordena(lista):
    for i in range(len(lista)):
        minimo = min(lista[i:])
        indi = lista.index(minimo)
        aux = lista[i]
        if lista[i] > minimo:
            lista[i] = minimo
            lista[indi] = aux 
    return lista

def busqueda(lista,valor):
    iz = lista.index(lista[0])
    der = lista.index(lista[-1])
    while iz <= der: 
        medio = (iz + der) // 2 #Doble diagonal para retornar solo entero
        if valor == lista[medio]:
            return medio
        elif valor < lista[medio]:
            der = medio - 1
        elif valor > lista[medio]:
            iz = medio + 1
    

listaB = ordena(lista)
print(busqueda(listaB,7))