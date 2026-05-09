from unittest.mock import right


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in(None,p,q): # 找到就不递归了，None说明没找到目标节点
            return root
        # 递归过程中把每个节点当成根节点从而移动
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)

        if left and right: # 如果左右子树都有目标节点
            return root

        return left or right
"""
先把两个点扫出来，根据他们到根节点的path找最近的公共节点，path包含本身
"""