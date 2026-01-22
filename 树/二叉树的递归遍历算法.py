import collections
# 二叉树节点的存储结构
class BNode(object):
    def __init__(self,data = None,lchild = None,rchild = None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild

class Btree(object):
    #创建根节点
    def __init__(self,root = None):
        self.root = root
    #先序遍历
    def PreOder(self,node):
        if node == None:
            return
        print(node.data)
        self.PreOder(node.lchild)
        self.PreOder(node.rchild)

    #中序遍历
    def MidOder(self,node):
        if node == None:
            return
        self.MidOder(node.lchild)
        print(node.data)
        self.MidOder(node.rchild)
    #后序遍历
    def PostOder(self,node):
        if node == None:
            return
        self.PostOder(node.lchild)
        self.PostOder(node.rchild)
        print(node.data)
    #统计叶子节点的个数
    def countleaf(self,node):
        if node == None:
            return
        if node.lchild == None and node.rchild == None:
            global n
            n = n + 1
        self.countleaf(node.lchild)
        self.countleaf(node.rchild)
    #层序遍历
    def levelOrder(self,root):
        if not root:
            return
        level = []
        queue = collections.deque([root])
        while queue:
            cur = queue.popleft()
            level.append(cur.data)
            print(cur.data)
            if cur.lchild:
                queue.append(cur.lchild)
            if cur.rchild:
                queue.append(cur.rchild)



if __name__ == "__main__":
    pass










