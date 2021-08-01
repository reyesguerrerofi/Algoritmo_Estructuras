
class Node():
    
    def __init__(self,data):
        self.data = data
        self.previous = None
        self.next1 = None
        
class DobleCircular():
    
    def __init__(self):
        self.first = None
        self.last = None
    
    def empty(self):
        return self.primero == None
    
    def add_first(self,data):
        if self.empty():
            self.first = self.last = Node(data)
        else:
            aux = Node(data)
            aux.next1 = self.first
            self.first.previous = aux
            self.first = aux
        self.__join_nodes()
    
    def add_last(self,data):
        if self.empty():
            self.first = self.last = Node(data)
        else:
            aux = self.last
            self.last = aux.next1 = Node(data)
            self.last.previous = aux
        self.__join_nodes()
    def __join_nodes(self):
        if self.first != None:
            self.first.previous = self.last
            self.last.next1 = self.first    
    
    def show_normal(self):
        aux = self.first
        while aux:
            print(aux.data)
            aux = aux.next1
            if aux == self.first :
                break
    def show_reverse(self):
        aux = self.last
        while aux:
            print(aux.data)
            aux = aux.previous
            if aux == self.last:
                break
    def delete_first(self):
        if self.empty():
            print("Empty list")
        elif self.first == self.last:
            self.first = self.last = None
        else:
            self.first = self.first.next1
        self.__join_nodes()
    def delete_last(self):
        if self.empty():
            print("Empty list")
        elif self.first == self.last:
            self.first = self.last = None
        else:
            self.last = self.last.previous
        self.__join_nodes()
        
    def search(self,data):
        aux = self.first
        while aux:
            if aux.data == data:
                return True
            else:
                aux = aux.next1
                if aux == self.first:
                    return False

lista = DobleCircular()

lista.add_last(12)