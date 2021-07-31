"""
Lista doblemente enlazada
se puede recorrer por ambas direcciones
"""
#!Codigo
class Nodo():
    
    def __init__(self,data):
        self.data = data
        self.next1 = None
        self.previous = None
        
        
class ListaDoble():
    
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
        
    def empty(self):
        return self.first == None
    
    def add_last(self,data):
        if self.empty():
            self.first = self.last = Nodo(data)
        else:
            aux = self.last
            self.last = aux.next1 = Nodo(data)
            self.last.previous = aux
        self.size += 1
    def add_first(self,data):
        if self.empty():
            self.first = self.last = Nodo(data)
        else:
            aux = self.first
            self.first = aux.previous = Nodo(data)
            self.first.next1 = aux
        self.size += 1

    def show_first(self):
        aux = self.first
        while aux:
            print(aux.data)
            aux = aux.next1
    def show_last(self):
        aux = self.last
        while aux:
            print(aux.data)
            aux = aux.previous
            
    def delete_first(self):
        if self.empty():
            print("Empty List")
        elif self.first.next1 == None:
            self.first = self.last = None
            self.size = 0
        else:
            self.first = self.first.next1 
            self.first.previous = None
            self.size -= 1
    def delete_last(self):
        if self.empty():
            print("Empty List")
        elif self.last.previous == None:
            self.last = self.first = None
            self.size = 0
        else:
            self.last = self.last.previous
            self.last.next1 = None
            self.size -= 1
    def tamano(self):
        print("List size: ",self.size)
lista = ListaDoble()

lista.add_last(12)
lista.add_last(10)
lista.add_last(20)
lista.add_first(1)
lista.add_first(5)

lista.show_first()
print("----------------")

lista.delete_last()
lista.show_first()

print("-----------")

lista.delete_first()
lista.show_first()

lista.tamano()

lista.add_first(23)
lista.add_last(22)
lista.tamano()