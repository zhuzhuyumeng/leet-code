# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        cnt = defaultdict(int)
        ans = 0
        cnt[0] = 1
        def dfs(root: Optional[TreeNode],count: int):
            nonlocal ans
            count += root.val
            ans += cnt[count-targetSum] # 维护终点，枚举起点
            cnt[count] += 1
            if root.left:
                dfs(root.left,count)
            if root.right:
                dfs(root.right,count)
            cnt[count] -= 1

        if root is None:
            return ans
        dfs(root,0)
        return ans