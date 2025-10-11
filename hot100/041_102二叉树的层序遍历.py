# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root is None:
            return []
        stack = [root]
        while stack:
            temp = []
            z = []
            for i in range(len(stack)):# 不可以用栈，因为要按顺序
                z.append(stack[i].val)
                if stack[i].left:
                    temp.append(stack[i].left)
                if stack[i].right:
                    temp.append(stack[i].right)
            z.reverse()
            res.append(z)
            stack = temp
        return res

        # if root is None:
        #     return []
        # dq = collections.deque([root])
        # result = []
        # while dq:
        #     level = []
        #     for _ in range(len(dq)):
        #         node = dq.popleft()
        #         if node.left:
        #             dq.append(node.left)
        #         if node.right:
        #             dq.append(node.right)
        #         level.append(node.val)
        #     result.append(level)
        # return result



"""
直接一个大拉
如何给堆栈计数，一层遍历完，下一层怎么算
1
2,3
4, , ,5
"""