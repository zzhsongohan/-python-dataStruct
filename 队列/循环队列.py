class queue(object):
    def __init__(self,MaxSize):
        #创建队列
        self.queque = [None]*MaxSize
        #队列容量大小
        self.maxsize = MaxSize
        #头指针，尾指针初始值
        self.front = 0
        self.rear  = 0

    #入队
    def Inqueque(self,item):
        #判断是否为满
        if(self.rear+1)%self.maxsize == self.front:
            print("队满")
        #不满则插入元素
        else:
            self.queque[self.rear] = item
            self.rear = (self.rear + 1)%self.maxsize
    #出队
    def Outqueque(self):
        #判空
        if self.front == self.rear:
            return None
        #不空则返回值
        else:
            item = self.queque[self.front]
            self.front = (self.front + 1)%self.maxsize
            return item
    #遍历
    def travel(self):
        p = self.front
        while p != self.rear:
            print(self.queque[p],end = " ")
            p = (p+1)%self.maxsize
        print("\n")
    #长度
    def getsize(self):
        count = (self.rear - self.front + self.maxsize)%self.maxsize
        return count



if __name__ == "__main__":
    temp_queque = queue(6)
    temp_queque.Inqueque(1)
    temp_queque.Inqueque(2)
    temp_queque.Inqueque(3)
    temp_queque.Inqueque(4)
    print(temp_queque.getsize())
    temp_queque.travel()
    temp_queque.Outqueque()
    temp_queque.Outqueque()
    temp_queque.travel()
    temp_queque.Outqueque()
    temp_queque.Outqueque()

