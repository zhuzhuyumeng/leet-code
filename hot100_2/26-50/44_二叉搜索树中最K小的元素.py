# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        node = root
        rst = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            rst.append(node.val)
            node = node.right

        return rst[k-1]
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = 0
        def dfs(node:Optional[TreeNode]):
            # 从根节点开始，往左子树，到底访问第一个节点，k-1，每访问一个是一个
            nonlocal k,ans
            if node is None:
                return
            dfs(node.left)
            k = k - 1
            if k == 0:
                ans = node.val
                return ans
            dfs(node.right)

        dfs(root)
        return ans