from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        # 递归边界结束条件
        if len(preorder)==0:
            return None
        root = TreeNode(preorder[0])
        if len(preorder)==1:
            return root
        index=0
        # 找到从中序序列中找到左右子树的划分
        inlength = len(inorder)
        for i in range(inlength):
            if root.val == inorder[i]:
                index = i
                break
        # 切分前中序队列，分成左右子树递归构造
        inleft = inorder[0:index]
        inright = inorder[index+1:]
        preleft = preorder[1:len(inleft)+1]
        preright = preorder[len(inleft)+1:]
        root.left = self.buildTree(preleft,inleft)
        root.right = self.buildTree(preright,inright)
        return root





"""
先序，根左右
中序，左根右
"""