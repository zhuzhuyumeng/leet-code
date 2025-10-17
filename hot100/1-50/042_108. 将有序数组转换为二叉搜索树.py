# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def ph(left: int,right: int):
            if left>right:
                return None
            mid = (left+right)/2
            tree = TreeNode(nums[mid])
            tree.left = ph(left,mid-1)
            tree.right = ph(mid+1,right)
            return tree
        return ph(0,len(nums)-1)


"""
[-10,-3,0,5,9]
递归，左右划分，就从头开始
"""