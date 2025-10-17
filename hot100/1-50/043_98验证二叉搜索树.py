# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        flag = True
        if root is None:
            return flag
        stack = []
        node = root
        pre = None
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if pre is not None and node.val<=pre.val:
                flag = False
            pre = node
            node = node.right # 右子树
        return flag


"""
左无右有
左右都有
左有右无
左右都无
会出现非严格的情况，仅对左右子树判断不够
        def real(root: Optional[TreeNode]) -> bool:
            if root.left is None and root.right is None: # 左右都无
                return True
            elif root.left is None and root.right is not None and root.right.val<=root.val: # 左无右有
                return False
            elif root.left is not None and root.left.val>=root.val and root.right is None: # 左有右无
                return False
            elif root.left is not None and root.left.val<root.val and root.right is None:
                isleft = real(root.left)
                isright = True
            elif root.left is None and root.right is not None and root.right.val > root.val:
                isleft = True
                isright = real(root.right)
            elif root.left.val>=root.val or root.right.val<=root.val:
                return False
            else:
                isleft = real(root.left)
                isright = real(root.right)
            return (isleft and isright)
        return real(root)
"""
