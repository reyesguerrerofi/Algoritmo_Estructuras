"""
Recursividad: Funcion que se llama a si misma
Como los factoriales 5! = 5*4*3*2*1 = 120
"""
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))

#Torres de Hanoi
"""
    Puedes mover solamente un disco a la vez.
    Ningún disco puede estar encima de un disco más pequeño. 
    Por ejemplo, si el disco 3 está en una varilla, 
    entonces todos los discos debajo del disco 3 deben tener números mayores que 3.
"""
