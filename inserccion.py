"""
Algoritmo de ordenamiento por inserccion
"""

lista = [7,4,5,3,10,9]

for i in range(1,len(lista)):
    actu = lista[i]
    j = i - 1 
    while j >= 0 and actu < lista[j]:
        lista[j+1] = lista[j]
        lista[j] = actu
        j -= 1
print(lista)