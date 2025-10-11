# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root is None:
            return res
        stack = [root]
        while stack:
            temp = []
            val = []
            for i in range(len(stack)):
                val.append(stack[i].val)
                if stack[i].left:
                    temp.append(stack[i].left)
                if stack[i].right:
                    temp.append(stack[i].right)
            res.append(val)
            stack = temp
        res.reverse()
        return res