#1..双亲节点类
class CNode(object):
    def __init__(self,data,parent):
        self.data = data
        self.parent = parent
########################################
#2..子节点表示法（孩子链表法）
# 0 A -> B C D
# 1 B -> D F
# 2 C -> G
# 3 D -> H I
# 4 F
# 5 G
# 6 H
# 7 I

#双亲节点类
class PNode(object):
    def __init__(self,data,firstchild = None):
        # 数据域
        self.data = data
        # 第一个子节点域
        self.firstchild = firstchild

# 孩子节点类
class cNode(object):
    def __init__(self,child,next=None):
        self.child = child
        self.next = next

#################################
#3..长子兄弟表示法
#节点的左指针指向它的第一个孩子（长子）
#节点的右指针指向它的下一个兄弟


#4.list递归实现








