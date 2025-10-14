# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def search(root: Optional[TreeNode], count: int):
            if root:
                count -= root.val
                path.append(root.val)
            if root.left is None and root.right is None and count==0:
                res.append(path.copy()) # 深拷贝一份，当前内容复制一份权限列表，再存入res，防止回溯时被擦除
            if root.left:
                search(root.left,count)
            if root.right:
                search(root.right,count)
            path.pop()
        
        if root is None:
            return res
        path = []
        search(root,targetSum)
        return res