# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def traversal(root: Optional[TreeNode],count: int)->bool:
            if root:
                count -= root.val
            if root.left is None and root.right is None and count == 0:# 在头结点为None时有问题
                return True
            if root.left is None and root.right is None:
                return False
            if root.left:
                if traversal(root.left,count): # 22-17
                    return True
            if root.right:
                if traversal(root.right,count):
                    return True
            return False

        if root is None:
            return False
        return traversal(root,targetSum)

"""
            5,
     4,             8,
  11,null       ,13   ,4,
7,2,        null,null,null,1]
"""