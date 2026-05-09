from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self,val=0,left=None,right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self,root:Optional[TreeNode])->int:
        if root is None:
            return []
        queue = deque([root])
        rst = []

        while queue:
            level_size = len(queue)
            tmp = []
            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                tmp.append(node.val)
            rst.append(tmp)
        return rst