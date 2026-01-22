class Node(object):
    def __init__(self,value=None):
        self.key = value
        self.color = None
        self.lchild = None
        self.rchild = None
        self.parent = None

class RB_tree(object):
    def __init__(self):
        self.root = None
        self.nil:Node = None

    def newNode(self,root,key):
        node = Node(key)
        node.color = 'RED'
        node.key = key
        node.lchild = root.nil
        node.rchild = root.nil
        node.parent = root.nil
        return node
    # 左旋函数
    def leftroate(self,T,root):
        new_root = root.rchild
        temp = new_root.lchild
        root.rchild = temp
    #     修改父节点
        if temp != T.nil:
            temp.parent = root
        #修改新根的父节点
        if root.parent == T.nil:
            T.root = new_root
        elif root == root.parent.lchild:
            root.parent.lchild = new_root

        elif root == root.parent.rchild:
            root.parent.rchild = new_root

        new_root.lchild = root
        root.parent = new_root

    def rightroate(self,T,root):
        new_root = root.lchild
        temp = new_root.rchild
        root.lchild = temp

        if temp != T.nil:
            temp.parent = root
        if root == root.parent.lchild:
            root.parent.lchild = new_root
            #
            new_root.parent = root.parent
        elif root == root.parent.rchild:
            root.parent.rchild = new_root
#
            new_root.parent = root.parent
        new_root.rchild = root
        root.parent = new_root

#     定义函数，插入新节点
    def rbtree_insert(self,T,z):
        Z =Node(z)
        Z.color = "RED"
        Z.lchild = T.nil
        Z.rchild = T.nil
        pre = T.nil
        cur = T.root
        while cur!=T.nil:
            pre = cur
            if Z.key<cur.key:
                cur = cur.lchild
            elif Z.key>cur.key:
                cur = cur.rchild
            else:#不插入相同的点
                return
        #插入节点

        #此时 pre是叶子节点，也是将要插入的节点的父节点
        Z.parent = pre

        #特殊情况，树空
        if pre == T.nil:
            T.root = Z
        #当Z小
        if Z.key<pre.key:
            pre.lchild = Z
        elif Z.key>pre.key:
            pre.rchild = Z
        self.rbtree_insert_fixup(T,Z)
    #调整插入后的失衡情况
    def rbtree_insert_fixup(self,T,u):
        #只有当插入节点的父节点为红色时才需要调整
        while u.parent.color == 'RED':
            #L X X
            if u.parent == u.parent.parent.lchild:
                #获取到插入节点的叔叔节点
                uncle = u.parent.parent.rchild
                #L X r:只需变色
                if uncle.color == "RED":
                    u.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    u.parent.parent.color = "RED"
                    #将u指向爷爷节点
                    u = u.parent.parent
                #L X b
                elif uncle.color == "BLACK":
                    #L R b
                    if u == u.parent.rchild:
                        #将LRb调整为LLb
                        u = u.parent
                        self.leftroate(u)
                     #L L b
                    u.parent.color = "BLACK"
                    u.parent.parent.color = "RED"
                    self.rightroate(u.parent.parent)
            # R X X
            elif u.parent == u.parent.parent.rchild:
                #获取叔叔节点
                uncle = u.parent.parent.lchild
                #R X r:只需变色
                if uncle.color == "RED":
                    u.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    u.parent.parent.color = "RED"
                    #将u指向u的爷爷节点
                    u = u.parent.parent
                #R X b
                elif uncle.color == "BLACK":
                    #R L b
                    if u == u.parent.lchild:
                        u = u.parent
                        self.rightroate(u)
                    #R R b
                    u.parent.color = "BLACK"
                    u.parent.parent.color = "RED"
                    self.leftroate(u.parent.parent)
        #要保证调整后的根节点为黑色
        T.root.color = "BLACK"
    def mid_travel(self,T,node):
        if node == T.nil:
            return
        self.mid_travel(T,node.lchild)
        print(node.key,"\n",node.color)
        self.mid_travel(T,node.rchild)

    def pre_travel(self,T,node):
        if node == T.nil:
            return
        print(node.key,"\n",node.color)
        self.pre_travel(node.lchild)
        self.pre_travel(node.rchild)

if __name__ == "__main__":
    keyArray = [10,50,60,62,65,70]
    rbtree = RB_tree()
    #定义外部节点
    rbtree.nil = Node()
    rbtree.nil.color = "BLACK"
    rbtree.root = rbtree.nil
    node = rbtree.nil
    for i in range(len(keyArray)):
        node = rbtree.newNode(rbtree,keyArray[i])
        rbtree.rbtree_insert(rbtree,keyArray[i])
        rbtree.mid_travel(rbtree,rbtree.root)











