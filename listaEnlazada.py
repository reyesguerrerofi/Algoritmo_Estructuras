"""
Lista enlazada
Accesos a los nodos mediante apuntadores
Se apunta al siguiente nodo en ua lista simple
"""

class Nodo():
    def __init__(self,data):
        self.data = data
        self.siguiente = None
        
#!Las listas siempre tienen un primer elemento 
#! o cabecera y un ultimo apuntando a None
class ListaS():
    def __init__(self):
        self.first = None
        self.last = None
    def empty(self):
        return self.first == None
    
    def add_last(self,dato):
        if self.empty():
            self.first = self.last = Nodo(dato)
            """Si la lista es vacia
            se agrega primer elemento, este es
            equivalente al primer y ultimo nodo"""
        else:
            """
            Como ya tiene un valor el nuevo nodo Aux
            es creado y como debe ser el ultimo el siguiente
            del antiguo nodo ultimo debe apuntar al nuevo nodo auxiliar
            y ahora self.ultimo es el auxiliar"""
            aux = self.last
            self.last = aux.siguiente = Nodo(dato)
            """aux = Nodo(dato)
                self.last.siguiente = aux
                self.ultimo = aux
            """
    def delete_last(self):
        aux = self.first
        while aux.siguiente != self.last:
            aux = aux.siguiente
        aux.siguiente = None
        self.last = aux
    def add_first(self,data):
        if self.empty():
            self.first = self.last = Nodo(data)
        else:
            aux = Nodo(data)
            aux.siguiente = self.first
            self.first = aux
    def delete_last(self):
        self.first = self.first.siguiente
    def access(self):
        aux = self.primero
        while aux != None:
            print(aux.dato)
            aux = aux.siguiente