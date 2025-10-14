# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(postorder) == 0:
            return None
        root = TreeNode(postorder[-1])
        if len(postorder) == 1:
            return root
        index = 0
        for i in range(len(inorder)):
            if root.val == inorder[i]:
                index = i
                break
        # 找到了中序的根节点位置
        inleft = inorder[0:index]
        inright = inorder[index+1:]
        postleft = postorder[0:len(inleft)]
        postright = postorder[len(inleft):len(postorder)-1]# 左闭右开
        root.left = self.buildTree(inleft,postleft)
        root.right = self.buildTree(inright, postright)
        return root
"""
中序。知根可分左右
后序。最后一个是根
可以把区间划分出来
1.后序
2.后序大小为1
3.根据后序的根节点去中序找
"""