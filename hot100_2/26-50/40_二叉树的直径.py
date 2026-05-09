from typing import Optional

class TreeNode:
    def __init__(self,val=0,left=None,right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self,root:Optional[TreeNode])->int:
        self.maxlen = 0
        def findmaxdepth(root:Optional[TreeNode])->int:
            if root is None:
                return 0
            leftheight = findmaxdepth(root.left)
            rightheight = findmaxdepth(root.right)
            self.maxlen = max(self.maxlen,leftheight+rightheight)
            return max(leftheight,rightheight)+1

        height = findmaxdepth(root)
        return self.maxlen

"""
左右高低差最大的和
"""