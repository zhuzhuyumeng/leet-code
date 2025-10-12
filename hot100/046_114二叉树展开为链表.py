# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        stack = [root]

        prev = None
        while stack:
            cur = stack.pop()
            if prev:
                prev.left = None
                prev.right = cur
            left,right = cur.left,cur.right
            if right:
                stack.append(cur.right)
            if left:
                stack.append(cur.left)
            prev = cur
            # 先右子树，后左子树，从而有左子树的子树先进
        return None


"""
我知道前序遍历，但是遍历完如何修改左右节点呢
左中右
prev节点存在，左节点已被遍历，右节点为当前节点
      x
    pre
cur
[1,2,5,3,4,null,6]
    1
 2    5
3 4 null 6
根节点的左子树完全消失了
"""