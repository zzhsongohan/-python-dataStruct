# 定义双链表的节点
class Node(object):
    def __init__(self,item):
        self.item = item
        self.next = None
        self.prev = None

class DoubleLinkList(object):
    def __init__(self):
        self.__head = None

    """判断列表是否为空"""

    def is_empty(self):
        return self.__head == None

    """链表长度"""

    def length(self):
        cur = self.__head  # 遍历指针cur指向第一个节点
        count = 0
        while cur != None:
            count = count + 1
            cur = cur.next
        return count

    """遍历链表"""

    def travel(self):
        cur = self.__head
        while cur != None:
            print(cur.item, end=" ")
            cur = cur.next

    """尾部添加节点"""

    def append(self, item):
        # 构造节点
        node = Node(item)
        # 情况一：若链表为空
        if self.is_empty():
            self.__head = node
        # 情况二，链表不为空
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    """在链表头部添加节点"""

    def add(self, item):
        node = Node(item)
        # 先将新节点链接在头节点，即虚拟头节点head所指向的节点
        if self.is_empty():
            self.__head = node
        else:
            node.next = self.__head
            self.__head.prev = node
            self.__head = node

    """在任意位置插入节点"""

    def insert(self, pos, item):
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
            while count <(pos-1):
                count = count + 1
                cur = cur.next
            node.prev = cur
            node.next = cur.next
            cur.next.prev = node
            cur.next = node


    """查找"""

    def search(self, item):
        cur = self.__head  # 指向头节点
        while cur != None:  # 不能是cur.next 因为最后一个节点的next为None，不进入循环，造成最后一个节点没有比较
            if cur.item == item:
                return True
            else:
                cur = cur.next
        return False

    """删除"""

    def remove(self, item):
        #若链表为空
        if self.is_empty():
            return
        else:
            cur = self.__head
            #若删除的是第一个节点
            if cur.item == item:
            #链表中只有这一个节点
                if cur.next == None:
                    self.__head = None
            #链表中有其他节点
                else:
                    cur.next.prev = None
                    self.__head = cur.next
                return
        #删除的是一般节点
            while cur != None:
                if cur.item == item:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                    break
                cur = cur.next

        #遍历到最后一个节点
            #找到要删除的节点后
                #该节点cur的前节点的next指向cur的下一个节点
                #该节点cur的后节点的prev指向cur的上一个节点

if __name__ == "__main__":
    dll = DoubleLinkList()
    dll.add(1)
    dll.add(2)
    dll.append(3)
    dll.insert(2,4)#2,1,4,3
    dll.travel()
    print(dll.length())#4
    print(dll.length())#4
    print(dll.search(3))
    print(dll.search(4))
    dll.remove(1)
    dll.travel()
