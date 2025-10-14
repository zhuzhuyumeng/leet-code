# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        cnt = defaultdict(int)
        ans = 0
        cnt[0] = 1
        s = 0
        flag = False
        def search(root: Optional[TreeNode], s: int) -> None:
            if root is None:
                return None
            nonlocal flag
            s+=root.val
            if s==targetSum and root.left is None and root.right is None:
                flag = True
            if root.left:
                search(root.left,s)
            if root.right:
                search(root.right,s)
            s-=root.val
        search(root,s)
        return flag

"""
         [5,
     4,             8,
  11,null       ,13   ,4,
7,2,        null,null,null,1]
"""