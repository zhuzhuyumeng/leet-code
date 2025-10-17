# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from base import height


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxlen = 0
        def getheight(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            leftheight = getheight(root.left)
            rightheight = getheight(root.right)
            self.maxlen = max(leftheight+rightheight,self.maxlen)
            height = max(leftheight,rightheight)+1
            return height,maxlen
        height,maxlen = getheight(root)
        return self.maxlen




"""
直径就是任意两个节点之间的最大长度，每个根节点的最大深度之和
如何存储呢，一个存最大，一个存和
"""