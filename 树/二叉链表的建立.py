class BNode(object):
    def __init__(self,data=None,lchild=None,rchild=None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild

#建立二叉树
class Btree(object):
    def __init__(self,root_data = None, lchild = None,rchild = None):
        self.root = BNode(root_data)
        self.root.lchild = lchild
        self.root.rchild = rchild

    # 先序遍历建立二叉树
    def preorder_create(self):
        Node_data = input("输入节点的数据，*表示空")
        if Node_data == '*':
            return None
        else:
            node = BNode(Node_data)
            node.lchild = self.preorder_create()
            node.rchild = self.preorder_create()
        return node
    # 获取叶子节点数目
    def countleaf(self,T):
        if T == None:
            return
        else:
            if T.lchild == None and T.rchild == None:
                global n
                n = n + 1
                return 1
            self.countleaf(T.lchild)
            self.countleaf(T.rchild)
    #查找元素
    def search(self,T,ch):
        if T == None:
            return
        if T.data == ch:
            return T
        else:
            p = self.search(T.lchild,ch)
            if p != None:
                return p
            p = self.search(T.rchild,ch)
            if p != None:
                return p



def preorder(T):
    if T == None:
        return
    print(T.data)
    preorder(T.lchild)
    preorder(T.rchild)
def  inorder(T):
    if T == None:
        return
    inorder(T.lchild)
    print(T.data)
    inorder(T.rchild)


if __name__ == "__main__":
    # a = BNode('A')
    # b = BNode('B')
    # c = BNode('C')
    # a.lchild = b
    # a.rchild = c
    # preorder(a)
    tree = Btree()
    tree.root = tree.preorder_create()
    preorder(tree.root)
    n = 0
    tree.countleaf(tree.root)
    print("叶子节点数：",n)
