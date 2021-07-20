"""
Colas:
Estructura FIFO(First In, First Out)
Operaciones: 
Insertar
Eliminar
Buscar 
Empty
Retorno elemento frontal
Tamaño Cola
"""

def Cola():
    
    def __init__(self):
        self.cola = []
        self.size = 0
    def empty(self):
        return len(self.cola) == 0
    
    def push(self,data):
        self.cola += [data]
        self.size += 1
    
    def pop(self):
        if self.empty():
            print(" Empty queue ")
        else:
            self.cola = [self.cola[i] for i in range(1,self.size)]
            self.size -= 1
    def mostrar(self):
        n = self.size - 1
        while n > -1:
            print("[%d]   =>  %d",(n,self.cola[n]))
            n -= 1
    def front(self):
        if self.empty():
            print("Empty")
        else:
            print(self.cola[0])
    
    