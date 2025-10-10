# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self, root: Optional[TreeNode], vec: List[int]):
        if root is None:
            return
        vec.append(root.val)
        self.preorder(root.left, vec)
        self.preorder(root.right, vec)
        return

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        List = []
        self.preorder(root, List)
        return List
