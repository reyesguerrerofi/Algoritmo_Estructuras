"""
Pilas
LIFO (Last In, First Out)
Operaciones:
Creacion
Push
Pop
Peek
Empty
Pueden ser estaticas o dinamicas
"""
#!Con POO

class PilaEstatica():
    
    def __init__(self,size):
        self.lista = []
        self.top = 0
        self.size = size
    
    def empty(self):
        if self.top == 0:
            return True
        else:
            return False
    
    def push(self,data):
        if self.top < self.size:
            self.lista += [data]
            self.top += 1
        else:
            print("Full Stack")
            #!Dinamica
            #?self.size += 1
            #?self.lista += [dato]
            #?self.tope += 1

    def pop(self):
        if self.empty():
            print("Empty stack")
        else:
            self.top -= 1
            self.lista = [self.lista[x] for x in range(self.top)]
    def peek(self):
        return self.lista[-1]
    

pila1 = PilaEstatica(4)

pila1.push(1)
pila1.push(2)
pila1.push(3)

print(pila1.peek())

pila1.pop()

print(pila1.peek())