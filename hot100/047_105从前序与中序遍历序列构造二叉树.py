# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        index = 0
        for i in range(len(inorder)):
            if root.val == inorder[i]:
                index = i
                break
        inleft = inorder[0:index]
        inright = inorder[index+1:]
        preleft = preorder[1:len(inleft)+1]
        preright = preorder[len(inleft)+1:]
        root.left = self.buildTree(preleft,inleft)
        root.right = self.buildTree(preright,inright)
        return root

"""
递归，
前序第一个是根节点。
中序可看出左右子树
如何利用这个特性进行递归？
主要依托哪个序列

"""