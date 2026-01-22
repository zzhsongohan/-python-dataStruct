class quequeHead(object):
    def __init__(self):
        self.front = None
        self.rear = None

class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkQueque(object):
    def __init__(self):
        #创建头节点
        self.__head = quequeHead()

    #判断空
    def is_empty(self):
        if self.__head.front == self.__head.rear and self.__head.front == None:
            return True
        else:
            return False
    #入队
    def Inqueque(self,data):
        node = Node(data)
        #若此时队链为空
        if self.is_empty():
            self.__head.front = node
            self.__head.rear  = node
        else:
            self.__head.rear.next = node
            self.__head.rear = node

    #出队
    def Outqueque(self):
        if self.is_empty():
            print("对链为空")
            return None
        #当只有一个节点
        if self.__head.front == self.__head.rear and self.__head.front != None:
            target = self.__head.front
            self.__head.front = None
            self.__head.rear = None
            return target
        else:
            target = self.__head.front
            self.__head.front = self.__head.front.next
            return target
    def tarvel(self):
        if self.is_empty():
            print("队链为空")
            return
        if self.__head.front == self.__head.rear and self.__head.front != None:
            print(self.__head.front.data)
        else:
            p = self.__head.front
            while p != self.__head.rear:
                print(p.data)
                p = p.next
            print(p.data)


if __name__ == "__main__":
    LQ = LinkQueque()
    LQ.Inqueque(1)
    LQ.Inqueque(2)
    LQ.Inqueque(3)
    LQ.tarvel()
    LQ.Outqueque()
    LQ.tarvel()
    LQ.Outqueque()
    LQ.Outqueque()
    LQ.tarvel()

