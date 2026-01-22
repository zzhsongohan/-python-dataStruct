class bst_Node(object):
    def __init__(self,data=None,lchild = None,rchild = None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild

class bst_tree(object):
    def __init__(self,root_data=None,lchild = None,rchild = None):#初始化时如果有传入数据则创立根节点
        if root_data != None:
            self.root = bst_Node(root_data)
            self.root.lchild = lchild
            self.root.rchild = rchild
        else:
            self.root = None
    #插入方法
    def insert(self,data):
        self.root = self._insert(self.root, data)

    def _insert(self,root,data):
        if  root == None:
            return bst_Node(data)
        else:
            if data > root.data:
                root.rchild = self._insert(root.rchild,data)
            else:
                root.lchild =  self._insert(root.lchild,data)
            return root

    #查找方法：
    # 递归实现
    def search(self,target):
        ret = self._search(self.root,target)
        return ret.data

    def _search(self,root,target):
        #当传入的树为空时
        if root == None:
            return None
        #当目标值小于当前节点，向左节点查找
        if root.data > target:
            return self._search(root.lchild,target)
        #当目标值大于当前节点
        elif root.data < target:
            return self._search(root.rchild,target)
        elif root.data == target:
            return root
        return None

    #迭代法
    def search2(self,target):
        cur = self.root
        while cur != None:
            if target > cur.data:
                cur = cur.rchild
            elif target < cur.data:
                cur = cur.lchild
            elif target == cur.data:
                return cur
        return None

    #删除方法
    def delete(self,target):
        return self._delete(self.root,target)

    def _delete(self,root,target):
        #当为空树
        if root == None:
            return None
        #不为空
        if target > root.data:
            root.rchild = self._delete(root.rchild,target)
            return root
        elif target < root.data:
            root.lchild = self._delete(root.lchild)
            return root
        if target == root.data:
            #当前节点无孩子
            if root.lchild == None and root.lchild == None:
                root = None
                return root
            #有左子树，无右子树
            elif root.lchild != None and root.lchild == None:
                root = root.lchild
            #有右子树，无左子树
            elif root.rchild == None and root.lchild == None:
                root = root.lchild
            elif root.child != None and root.lchild != None:
                #若选择用左孩子代替该节点
                #则将该节点的右子树链接到左子树最右节点的右节点
                cur = root.lchild
                while cur.right != None:
                    cur = cur.right
                cur.rchild = root.rchild

    def midorder(self,T):
        if T is None:
            return []
        result = []
            # 递归过程：根 -> 左子树 -> 右子树
        result.extend(self.midorder(T.lchild))
        result.append(T.data)
        result.extend(self.midorder(T.rchild))
        return result

if __name__ == "__main__":
    list = [2,3,1,5,4,8]
    bstTree = bst_tree()
    for _ in list:
        bstTree.insert(_)
    ret = bstTree.midorder(bstTree.root)
    print(ret)
    res = bstTree.search(5)
    print(res)
    res2 = bstTree.search2(4)
    print(res2.data)
    bstTree.delete(8)
    ret3 = bstTree.midorder(bstTree.root)
    print(ret3)





