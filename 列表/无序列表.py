class Node:
     # 构造器

     # 代表一个节点
     def __init__(self,node_data):
         self._data = node_data
         self._next = None

    # 获取节点数据
     def get_data(self):
        return self._data

    # 设置节点数据
     def set_data(self,node_data):
        self._data = node_data
    #运用property
     data = property(get_data,set_data)

    #  获取下一个节点
     def get_next(self):
        return self._next
    #  设置下一个节点
     def set_next(self,node_next):
        self._next = node_next

     next = property(get_next,set_next)
    # 返回数据
     def __str__(self):
         return str(self._data)


# temp = Node(93)
# print(temp.data)


# 创建unorderList类管理节点
class unorderList:
    def __init__(self):
        self.head = None
    def add(self,item):
        if head == None:
            head.next = item
            item.next = None
        temp = head.next
        while true:
            if item.next == None:
                break


