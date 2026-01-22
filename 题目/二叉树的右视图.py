import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root):
        queue = collections.deque([root])
        if not root:
            return []
        ret = []
        while queue:
            temp_length = len(queue)
            for _ in range(temp_length):
                temp_level = []
                cur = queue.popleft()
                temp_level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            ret.append(temp_level.pop())
        return ret


