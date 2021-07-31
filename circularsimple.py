"""
Lista circular simple
Es similar a una lista enlazada simple pero el nodo final apunta al primer nodo
Se pueden insertar nodos desde uno del que se tenga referencia
Se puede acceder al primer nodo desde el apuntador del ultimo
"""

class Nodo():
    def __init__(self,data):
        self.data = data
        self.next1 = None

class ListaCircular():
    def __init__(self):
        self.first = None
        self.last = None
    
    def empty(self):
        return self.first == None #Regresa true si se cumple
    
    def add_first(self,data):
        if self.empty():
            self.first = self.last = Nodo(data)
        else:
            
            aux = Nodo(data)
            aux.next1 = self.first
            self.first = aux
            self.last.next1 = self.first
            
            """
            aux = self.first
            self.first = aux.next1 = Nodo(data)
            self.last.next1 = self.first
            """
    def add_last(self,data):
        if self.empty():
            self.first = self.last = Nodo(data)
        else:
            aux = self.last 
            self.last= aux.siguiente = Nodo(data)
            self.last.next1 = self.first
    
    
    def delete_first(self):
        if self.empty():
            print("Empty List")
        elif self.first == self.last:
            self.first = self.last = None
        else:
            self.first = self.first.next1
            self.last.next1 = self.first
    def delete_last(self):
        if self.empty():
            print("Empty List")
        elif self.first == self.last:
            self.first = self.last = None
        else:
            aux = self.first
            while aux.next1 != self.last:
                aux = aux.next1
            aux.next1 = self.first
            self.last = aux
    def show(self):
        aux = self.first
        while aux:
            print(aux.data)
            aux = aux.next1
            if aux == self.first:
                break


lista = ListaCircular()


lista.add_last(45)
lista.add_first(23)
lista.add_first(22)
lista.add_first(25)

lista.show()

lista.delete_last()

print("----")
lista.show()

lista.delete_first()

print("*"*25)

lista.show()


print("first:  ", lista.first.data)
print("last: ", lista.last.data)
print("last.next1 apunta a: ", lista.last.next1.data)