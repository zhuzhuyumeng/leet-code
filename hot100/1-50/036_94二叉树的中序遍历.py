# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root: Optional[TreeNode],vec: List[int]):
        if root is None:
            return
        self.inorder(root.left)
        vec.append(root.val)
        self.inorder(root.right)
        return


    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        list = []
        self.inorder(root,list)
        return list