from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightView(self,root:Optional[TreeNode])->list[int]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        rst = []
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i==n-1:
                    rst.append(node.val)
        return rst