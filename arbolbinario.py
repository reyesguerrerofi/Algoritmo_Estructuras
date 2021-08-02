"""
Arbol binario
Operaciones:
Empty
Add
Delete
Search
Size
Travesing:
    Pre-order
    Pos-order
    In-order
"""

class Node():
    
    def __init__(self,value = None, parent=None,is_root = False, is_left = False, is_right = False):
        self.value= value
        self.left = None
        self.right = None
        self.parent =  parent
        self.is_root = is_root
        self.is_left = is_left
        self.is_right = is_right
        
class binary_tree():
    
    def __init__(self):
        self.root = None
    
    def empty(self):
        return self.root == None
    
    def add(self,value):
        if self.empty():
            self.root = Node(value, is_root=True)
        else:
            node = self.__get_place(value)
            if value <= node.value:
                node.left = Node(value=value, parent=node, is_left=True)
            else:
                node.right = Node(value=value,parent=node,is_right=True)
    def __get_place(self,value):
        aux = self.root
        #!Se recorre el arbol
        while aux is not None:
            temp = aux
            if value <= aux.value:
                aux = aux.left
            else:
                aux = aux.right
        return temp
    def show_in_order(self,node):
        if node:
            self.show_in_order(node.left)
            print(node.value)
            self.show_in_order(node.right)
            
    
    def show_pre_order(self,node):
        if node:
            print(node.value)
            self.show_pre_order(node.left)
            self.show_pre_order(node.right)
    
    def show_pos_order(self,node):
        if node:
            self.show_pos_order(node.left)
            self.show_pos_order(node.right)
            print(node.value)
    def delete(self,value):
        pass
    def search(self,value,node):
        if node == None:
            return None
        else:
            if node.value == value:
                return node
            elif value <= node.value:
                return node.search(value,node.left)
            else:
                return self.search(value,node.right)

arbol = binary_tree()

arbol.add(8)
arbol.add(10)
arbol.add(3)
arbol.add(14)

arbol.show_in_order(arbol.root)

