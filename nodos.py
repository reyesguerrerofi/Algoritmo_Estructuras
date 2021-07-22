"""
Nodos
"""

class Node():
    def __init__(self,data,next1 = None):
        self.data = data
        self.next1 = next1
    #! -> es una anotacion de lo que regresa
    def __str__(self) ->str: #Regresa en un str un dato enviado
        return str(self.data)
    
    
def access(nodo):
    while nodo != None:
        print(nodo.data)
        nodo = nodo.next1
nodo4 = Node(10)
nodo3 = Node(20,nodo4)
nodo2 = Node(30,nodo3)
nodo1 = Node(40,nodo2)
nodo0 = Node(50,nodo1)

access(nodo2)



