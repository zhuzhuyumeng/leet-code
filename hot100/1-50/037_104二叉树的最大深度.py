# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def getheight(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            leftheight = getheight(root.left)
            rightheight = getheight(root.right)
            return max(leftheight,rightheight)+1
        return getheight(root)

"""
深度，层序遍历完的次数是不是
"""