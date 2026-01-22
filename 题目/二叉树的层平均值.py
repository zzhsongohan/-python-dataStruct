# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root):
        avg = []
        if root == None:
            return []
        queue = collections.deque([root])
        while queue:
            temp_length = len(queue)
            temp_level = []
            for _ in range(temp_length):
                cur = queue.popleft()
                temp_level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            temp_avg = sum(temp_level)/temp_length
            avg.append(temp_avg)
        return avg


