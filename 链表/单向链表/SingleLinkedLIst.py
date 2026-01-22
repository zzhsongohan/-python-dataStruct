"""节点的实现"""

class SingleNode(object):
    def __init__(self,item):
        # 数据区域
        self.item = item
        #下一个节点
        self.next = None

"""单链表"""
class SingleLinkList(object):

    # 创建头节点
    def __init__(self):
        self.__head = None

    """判断列表是否为空"""
    def is_empty(self):
        return self.__head == None


    """链表长度"""
    def length(self):
        cur = self.__head#遍历指针cur指向第一个节点
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
    def append(self,item):
        #构造节点
        node = SingleNode(item)
        # 情况一：若链表为空
        if self.is_empty():
            self.__head = node
        # 情况二，链表不为空
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    """在链表头部添加节点"""
    def add(self,item):
        node = SingleNode(item)
        #先将新节点链接在头节点，即虚拟头节点head所指向的节点
        node.next = self.__head
        #再将虚拟头节点head指向node、
        self.__head  = node
    """在任意位置插入节点"""
    def insert(self,pos,item):
        node = SingleNode(item)
        """假设起始位置从0开始"""
        #特殊情况1，当插入位置为0或者小于0
        if pos <= 0:
            self.add(item)
        #特殊情况2，插入位置大于（链表长度-1）
        elif pos > (self.length()-1):
            self.append(item)
        #正常情况
        else:
            pre = self.__head#指向第一个节点
            count = 0
            while count < (pos - 1):
                count = count+1
                pre = pre.next
            node.next = pre.next
            pre.next = node

    """查找"""
    def search(self,item):
        cur = self.__head#指向头节点
        while cur != None:#不能是cur.next 因为最后一个节点的next为None，不进入循环，造成最后一个节点没有比较
            if cur.item == item:
                return True
            else:
                cur = cur.next
        return False
    """删除"""
    def remove(self,item):
        """双指针法"""
        pre = None#后指针
        cur = self.__head#前指针
        while cur != None:
            if cur.item == item:
                if cur == self.__head:                                                           
                    #如果删除的是头节点，则不应该操作pre，应该操作head指向第二个节点
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                cur = cur.next
            else:
                pre = cur
                cur = cur.next




if __name__ == "__main__":
    ll = SingleLinkList()
    print(ll.is_empty())
    print(ll.length())
    # ll.travel()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.add(8)
    ll.insert(-1,9)#98123456
    ll.insert(2,100) #9 8 100 1 2 3 4 5 6
    # ll.travel()
    ll.remove(100)
    ll.remove(9)
    ll.travel()#8 100  1 2 3 4 5 6
    print("test_finish")


