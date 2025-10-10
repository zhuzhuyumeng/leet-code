# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = list()
        if root is None:
            return res
        stack = []
        node = root
        while node or stack: # 有没有node为None，stack还存在的情况？整个左链压入栈中，再为左节点是空
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.left
                # 为空了，弹出栈顶节点，再转向右
            node = stack.pop()
            node = node.right # 单左链会使得node在出栈时全为空
        return res
"""
res作为列表
stack作为存放节点的栈
中左一直放到栈里面，如果没有再左，就从栈弹出那个节点找他的右，再继续

"""