from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import defaultdict


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0
        cnt = defaultdict(int)# 注意int初始化，自动返回默认0
        ans = 0
        cnt[0] = 1 # 第一个数字前缀和为0方便计算
        def search(root:Optional[TreeNode],s:int):
            nonlocal ans
            s+=root.val # s当前位置前缀和
            ans += cnt[s-targetSum] # 当前和-前缀和计算当前符合条件的个数
            cnt[s]+=1
            if root.left:
                search(root.left,s)
            if root.right:
                search(root.right,s)
            cnt[s]-=1

        search(root,0)
        return ans



"""
根左右，向下计算前缀和，
如何向下的时候互不影响？使用的时候+，不用的时候去掉
"""