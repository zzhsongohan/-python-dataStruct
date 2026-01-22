class val_Node(object):
    def __init__(self,data = None,lchild = None,rchild = None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild
        self.height = 1


class val_tree(object):
    def __init__(self,root_data = None,lchild = None,rchild = None):
        self.root = val_Node(root_data)


#获取树的高度
    def getheight(self,root):
        if(root == None):
            return 0
        return root.height
    #获取平衡因子
    def get_balance(self,node):
        return self.getheight(node.lchild)-self.get_balance(node.rchild)

    def max_height(self,height1,height2):
        return height1 if height1>height2 else height2

#定义左旋函数
#当前节点的右子树作为新的根节点
#     当前节点会作为新的根节点的左子树
#       如果新的根节点原来有左子树，则原来的左子树作为旧节根节点的右子树

    def leftRoate(self,root):
    #生成新的根节点指向当前节点的右子树
        new_root = root.rchild
        #暂时取出新根节点的左子树
        temp = new_root.lchild
        #当前节点作为新根节点的左孩子
        new_root.lchild = root
        #暂时存储的新根节点的左子树接到当前节点的右子树上
        root.rchild = temp
        #更新root和new_root的树高
        root.height = 1 + self.max_height((self.getheight(root.lchild)),(self.getheight(root.rchild)))
        new_root.height = 1 + self.max_height((self.getheight(new_root.lchild)),self.getheight(new_root.rchild))

        return new_root

# 定义右旋函数
    def rightRoate(self,root):
        #生成新的节点指向当前节点的左子树
        new_root = root.lchild
        #暂存新的根节点的右子树
        temp = new_root.rchild
        #当前节点作为新的根节点的右子树
        new_root.rchild = root
        #暂存的新根节点的右子树连接到当前节点的左子树上
        root.lchild = temp
        #更新root和new_root的树高
        root.height = 1 + self.max_height((self.getheight(root.lchild)), (self.getheight(root.rchild)))
        new_root.height = 1 + self.max_height((self.getheight(new_root.lchild)), self.getheight(new_root.rchild))

        return new_root
# 定义插入节点的函数
    # 插入节点，并调整树
    def insert_node(self,val):
        return self._insert_node(self.root,val)

    def _insert_node(self, node, val):
        if node == None:
            return val_Node(val)
        if val < node.data:
            node.lchild = self._insert_node(node.lchild,val)
        elif val > node.data:
            node.rchild = self._insert_node(node.rchild,val)
        else:
            return #不坐改变
        #更新树高
        node.height = 1 + self.max_height(self.getheight(node.lchild),self.getheight(node.rchild))

        #当前节点的平衡因子
        balance = self.get_balance(node)
        #失衡类型 LL型，LR型，RR型，RL型

        # LL型
        if(balance>1 and self.get_balance(node.lchild)>0):
            return self.rightRoate(node)
        #LR型
        elif (balance>1 and self.get_balance(node.lchild)<0):
            node.lchild = self.leftRoate(node.lchild)
            return self.rightRoate(node)
        #RR型
        elif (balance<-1 and self.get_balance(node.rchild)<0):
            return self.leftRoate(node)
        elif (balance<-1 and self.get_balance(node.rchild)>0):
            node.rchild = self.rightRoate(node.rchild)
            return self.leftRoate(node)

        return node
if __name__ == "__main__":
    pass





