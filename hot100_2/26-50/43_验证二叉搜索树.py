import sys
from typing import Optional
from unittest.mock import right


class TreeNode:
    def __init__(self,val = 0, left=None,right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self,root:Optional[TreeNode])->bool:
        if root is None:
            return True
        stack = []
        node = root
        pre = None
        # 树还能往下，栈还有祖先节点
        while stack or node:
            # 一路向左
            while node:
                stack.append(node)
                node = node.left
            # 弹出最左节点处理
            node = stack.pop()
            # 第一个是没有pre的，后面就是和前一个节点比
            if pre is not None and node.val<=pre.val:
                return False
            pre = node
            node = node.right #这不会遇到空的节点吗，！会在上面node为空从栈中弹出节点使用
        return True
    def isValidBST2(self,root:Optional[TreeNode])->bool:
        self.pre = -float('inf')
        def Valid(root:Optional[TreeNode])->bool:
            if root is None:
                return True
            if not Valid(root.left): # =F
                return False
            if root.val<=self.pre:
                return False
            self.pre = root.val
            # 访问右子树
            return Valid(root.right)

        return Valid(root)
