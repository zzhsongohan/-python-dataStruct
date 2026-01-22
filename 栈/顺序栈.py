class ArrayStack:
    def __init__(self, maxsize):
        self.maxsize
        self.stack = []
        self.top = -1

    def ArrayStack(self, maxsize):
        self.maxsize = maxsize
        self.stack = [maxsize]

    def isfull(self):
        return self.top == self.maxsize - 1

    def isempty(self):
        return self.top == -1

    def push(self, value):
        if self.isfull():
            print("栈满")
        self.top += 1
        self.stack[self.top] = value

    def pop(self):
        if self.isempty():
            raise Exception("栈空")
        data = self.stack[self.top]
        self.top -= 1

    def show(self):
        if self.isempty():
            print("栈空")
        else:
            for i in range(self.top, -1, -1):
                print(self.stack[i])

