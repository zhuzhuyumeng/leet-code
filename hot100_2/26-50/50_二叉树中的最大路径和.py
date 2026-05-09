from typing import Optional
from unittest.mock import right


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.maxSum = float("-inf") #负无穷
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def maxGain(root:Optional[TreeNode]):
            if root is None:
                return 0
            leftGain = max(maxGain(root.left),0)
            rightGain = max(maxGain(root.right),0)
            self.maxSum = max(self.maxSum,root.val+leftGain+rightGain)
            return root.val + max(leftGain,rightGain) #找最大的一边子树返回给父节点使用

        maxGain(root)
        return self.maxSum


"""
从底部开始计算，两边的最大和
"""