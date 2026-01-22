from collections import deque

queue = deque()
queue.append('cat')
queue.append('dog')
queue.append('tiger')

print(queue)
#从队头出
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())



