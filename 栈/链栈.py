class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack(object):
    def __init__(self):
        self.__top = None

    def is_empty(self):
        return self.__top == None

    def pushStack(self,item):
        node = Node(item)
        node.next = self.__top
        self.__top = node
    def popStack(self):
        p = self.__top
        self.__top = self.__top.next
        return p.data



if __name__ == "__main__":
    s = Stack()
    s.pushStack(1)
    s.pushStack(2)
    s.pushStack(3)
    print(s.popStack())
    print(s.popStack())
    print(s.popStack())