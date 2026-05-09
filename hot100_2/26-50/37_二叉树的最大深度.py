from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self,root:Optional[TreeNode])->int:
        # 感觉用层序遍历好一点
        if root is None:
            return 0
        queue = deque([root])
        height = 0
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            height +=1
        return height