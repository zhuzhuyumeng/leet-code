# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root is None:
            return res
        deque = collections.deque([root])
        while deque:
            level = []
            for _ in range(len(deque)):
                cur = deque.popleft()
                level.append(cur.val)
                if cur.left:
                    deque.append(cur.left)
                if cur.right:
                    deque.append(cur.right)
            res.append(level[-1])
        return res


"""
其实就是层次遍历的每层最后一个节点
"""