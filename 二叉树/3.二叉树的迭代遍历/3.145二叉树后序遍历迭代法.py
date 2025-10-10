# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = list()
        if root is None:
            return res
        stack = []
        node = root
        prev = None
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if node.right is None or node.right == prev:
                res.append(node.val)
                prev = node
                node = None # 这个点走过了，走栈
            else:
                stack.append(node)
                node = node.right
        return res
    # 这个左右的话左while接右while不合适吧
    # 需要判断右节点有没有，有没有走过