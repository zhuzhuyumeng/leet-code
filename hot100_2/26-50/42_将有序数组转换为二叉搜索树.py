from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        def ph(left,right):
            if left>right:
                return None
            mid = (left+right)//2
            root = TreeNode(nums[mid])
            root.left = ph(left,mid-1)
            root.right = ph(mid+1,right)
            return root

        return ph(0,len(nums)-1)



"""
[-10,-3,0,5,9]
递归，左右划分，就从头开始
"""