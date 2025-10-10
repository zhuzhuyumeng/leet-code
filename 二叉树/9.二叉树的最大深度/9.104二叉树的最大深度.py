# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def getHeight(root: Optional[TreeNode]) ->int:
            if root is None:
                return 0
            leftheight = getHeight(root.left)
            rightheight = getHeight(root.right)
            height = 1+max(leftheight,rightheight)
            return height
        return getHeight(root)