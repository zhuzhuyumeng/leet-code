from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return None
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
            if stack: # 指向下一个
                cur.right = stack[-1]
            # cur.right = cur.left if cur.left else cur.right # 丢失了左子树的引用
            cur.left = None
        return root


"""
先序遍历
右指针作为next指针
"""