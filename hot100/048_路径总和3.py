# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = 0
        cnt = defaultdict(int)
        cnt[0] = 1
        def search(root: Optional[TreeNode],s: int) -> None:
            if root is None:
                return
            s += root.val
            nonlocal ans
            ans +=cnt[s-targetSum] # 以当前节点的前缀减去目标值，剩下的
            """target = 7
                1
               2
              3
             4
            5
            """
            cnt[s]+=1
            if root.left:
                search(root.left,s)
            if root.right:
                search(root.right,s)
            cnt[s]-=1
            # 其实就只是在前序遍历加了数值
        search(root,0)
        return ans

"""
        cnt = defaultdict(int)
        cnt[0] = 1
        ans = 0 # 符合条件的个数
        s = 0 # 统计和
        if root is None:
            return None
        stack = [root]
        while stack:
            curr = stack.pop()
            s+=curr.val
            ans+=cnt[s-targetSum]
            cnt[curr.val]+=1
            left,right = curr.left,curr.right
            if right:
                stack.append(right)
            if left:
                stack.append(left)
        # 如何在合适的时机消除影响，如果该节点到底了，为叶子节点。值交给谁保持
"""



"""
节点根左右，先序遍历，过程中对结果求和，前缀和？
每个子树都要有前缀和
如果把前缀和放在哈希中，如何动态修改前缀和呢？即我们向下遍历终点时，怎么确定他的起点
在对一个节点递归结束后，可以消除他对哈希表的添加啊
"""