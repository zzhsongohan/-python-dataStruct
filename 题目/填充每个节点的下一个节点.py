# Definition for a Node.
import collections
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
#方法1：层序遍历法
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        queue = collections.deque([root])
        if not root:
            return []
        while queue:
            temp_level = []
            temp_length = len(queue)
            for _ in range(len(queue)):
                cur = queue.popleft()
                temp_level.append(cur.val)
                if _+1 == temp_length:
                    cur.next = None
                else:
                    cur.next = queue(0)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return root


