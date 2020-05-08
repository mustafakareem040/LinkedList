class Node:
    def __init__(self, value, next_value=None):
        self.value = value
        self.next = next_value
    def getvalue(self):
        return self.value
    def getnext(self):
        return self.next
    def setnext(self,data):
        self.next = data
    def setvalue(self,data):
        self.value = data
class LinkedList:
    def __init__(self,value):
        self.head = Node(value)
    def append(self,value):
        node = Node(value)
        node.setnext(self.head)
        self.head = node
    def search(self,value):
        node = self.head
        while node:
            if node.value == value:
                print(value)
                break
            node = node.next
        else:
            raise ValueError('Not Found')
    def showall(self):
        node = self.head
        while node:
            if node.next: print(node.value, end=',')
            else: print(node.value,end='')
            node = node.next
    def test(self):
        node = self.head
        while node:
            if node.prev: print(node.value)
            node = node.prev
