class Node(object):
    def __init__(self,item):
        self.item = item
        self.next = None

class SingleCycLinkedList(object):
    def __init__(self,node = None):
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        return self.__head == None


    def length(self):
        if self.is_empty():
            return 0
        count = 1
        cur = self.__head
        while cur.next != self.__head:
            cur = cur.next
            count = count + 1
        return count
    def travel(self):
        if self.is_empty():
            return
        else:
            cur = self.__head
            while cur.next != self.__head:
                print(cur.item,end = " ")
                cur = cur.next
            print(cur.item)
    def add(self,item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        cur = self.__head
        node.next = self.__head
        while cur.next != self.__head:
            cur = cur.next
        cur.next = node
        self.__head = node


    def append(self,item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            cur.next = node

    def insert(self,pos,item):
        node = Node(item)
        """假设起始位置从0开始"""
        # 特殊情况1，当插入位置为0或者小于0
        if pos <= 0:
            self.add(item)
        # 特殊情况2，插入位置大于（链表长度-1）
        elif pos > (self.length() - 1):
            self.append(item)
        # 正常情况
        else:
            cur = self.__head
            count = 0
            while count < (pos - 1):
                count = count + 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def search(self,item):
        if self.is_empty():
            return False
        cur = self.__head
        if cur.item == item:
            return True
        while cur.next != self.__head:
            cur = cur.next
            if cur.item == item:
                return True
        return False

    def remove(self,item):
        if self.is_empty():
            return
        prev = None
        cur = self.__head
        #若头节点为删除节点
        if cur.item == item:
            #若不止一个节点
            if cur.next != self.__head:
                #找到尾节点，指向第二个节点，接着将头节点只想第二个节点
                while cur.next != self.__head:
                    cur = cur.next
                cur.next = self.__head.next
                self.__head = self.__head.next
            #若只有一个接节点
            else:
                self.__head = None
        # 若删除的不是头节点
        else:
            prev = self.__head
            #移动到尾节点
            while cur.next != self.__head:
                #若找到删除节点
                if cur.item == item:
                    #前指针指向cur的下一个节点
                    prev.next = cur.next
                    cur = cur.next


                else:
                    prev = cur
                    cur = cur.next
        #若删除的是尾节点
            if cur.item == item:
                prev.next = cur.next
                return


if __name__ == "__main__":
    cll = SingleCycLinkedList()
    print(cll.is_empty())
    print(cll.length())
    cll.add(1)
    cll.add(2)
    cll.append(3)
    cll.insert(2,4)
    cll.insert(3,1)
    cll.remove(1)
    cll.remove(3)
    cll.travel()
