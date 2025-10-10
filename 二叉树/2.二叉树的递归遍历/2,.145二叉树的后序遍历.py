# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def post(root: Optional[TreeNode]):
            if root is None:
                return None
            post(root.left)
            post(root.right)
            List.append(root.val)

        if root is None:
            return None
        List = []
        post(root)
        return List

    # 左右都要走到底，放在栈中，左右出栈后才到根节点