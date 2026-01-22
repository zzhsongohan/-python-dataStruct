class Node(object):
    def __init__(self,data):
        self.lchild = None
        self.rchild = None
        self.data = data
        self.parent = None

#将n个叶子节点数据存放在列表中（append方法）
#将n个节点的数据进行排序
#取出最小的两个元素，作为左右子树
#从列表中删除这两个元素，并将新生成的节点添加到列表中
class create_huffman_tree(object):
    def __init__(self,nodes):
        self.root = None
        nodelist = nodes[:]
        while len(nodelist) > 1:
            nodelist.sort(key = lambda item:item.data)
            node_left = nodelist.pop(0)#取出列表中第一个最小值，并从列表中删除
            node_right = nodelist.pop(0)
            # 构建一个父节点
            node_farther = Node(node_left.data+node_right.data)
            node_farther.lchild = node_left
            node_farther.rchild = node_right
            # 将左右孩子的父节点指向构建的父节点
            node_right.parent = node_farther
            node_left.parent = node_farther
            nodelist.append(node_farther)
        self.root = nodelist[0]
        self.root.parent = None


    # 遍历查看
    def midorder(self,T):
        if T == None:
            return
        print(T.data)
        self.preorder(T.lchild)
        self.preorder(T.rchild)

    def huffman_encoding(self,nodes):
        if not self.root:
            return []
        huffman_code = ['']*len(nodes)
        for i in range(len(nodes)):
            node = nodes[i]
            while node != self.root:
                # 若为左节点，则为0，若为右节点，则为1
                if node.parent.lchild == node:
                    huffman_code[i] = '0' + huffman_code[i]
                else:
                    huffman_code[i] = '1' + huffman_code[i]
                node = node.parent

        return huffman_code

if __name__ == "__main__":
    haffnode = []
    # while True:
    #     a = int(input("输入叶子节点的权值，输入-1时结束"))
    #     if a == -1:
    #         break
    #     haffnode.append(Node(a))
    # haffmanTree = create_huffman_tree(haffnode)
    # if haffmanTree.root:
    #     haffmanTree.preorder(haffmanTree.root)
    char_frequence = [('T',7),(':',5),('A',2),('C',4)]
    for i,j in char_frequence:
        haffnode.append(Node(j))
    haffmanTree = create_huffman_tree(haffnode)
    haffman_Code = haffmanTree.huffman_encoding(haffnode)
    for i in haffman_Code:
        print(i)



