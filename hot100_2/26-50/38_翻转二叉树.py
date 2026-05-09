from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self,value=0,left=None,right = None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def invertTree(self,root:Optional[TreeNode]):
        if root is None:
            return None
        queue = deque([root])

        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                node.left,node.right = node.right,node.left
        return root