# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root):
        if root == None:
            return []
        result = []
        queue = []
        queue.append(self.root)
        while queue:
            temp_level = []
            temp_length = queue.len
            for _ in range(temp_length):
                cur = queue.pop(0)
                temp_level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            result.append(temp_level)
        return result



