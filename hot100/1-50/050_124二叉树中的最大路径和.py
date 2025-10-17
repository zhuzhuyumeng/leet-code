# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = -sys.maxsize
        def Gain(root: Optional[TreeNode]):
            if root is None:
                return 0
            left = max(Gain(root.left),0)
            right = max(Gain(root.right),0)

            self.maxSum = max(self.maxSum,(left+right+root.val))
            return max(left,right)+root.val
        Gain(root)
        return self.maxSum

        maxSum = -sys.maxsize
        def findmax(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            nonlocal maxSum
            leftmax = max(findmax(root.left),0)
            rightmax = max(findmax(root.right),0)
            maxSum = max(maxSum,leftmax+rightmax+root.val)
            return max(leftmax,rightmax)+root.val
        if root is None:
            return None
        if root.left is None and root.right is None:
            return root.val

        return findmax(root)



"""
并非最大前缀和，这有动态规划吗？
递归找每个节点子树的最大值
如果只有一个节点，是没有左右的0的
如果是负值，0是不对的
！从一个节点出发到另一个结点
可以左右子树同时，但是那是从根节点开始的，根节点不能走子树两次，即不能在子树再分叉
"""