# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(root: 'TreeNode',target: 'TreeNode')->list[TreeNode]:
            if root is None:
                return None
            path.append(root)
            if root == target: # 找到目标节点就返回
                return path.copy()
            if dfs(root.left,target) or dfs(root.right, target): # 有返回值就有对应的path
                return path.copy()
            path.pop()
            return None


        path = []
        path1 = dfs(root,p)
        path = []
        path2 = dfs(root,q)
        if not path1 or not path2:
            return None
        lca = None
        for u,v in zip(path1,path2): # 按位比较，以最短的比
            if u == v:
                lca = u
        return lca
"""
先把两个点扫出来，根据他们到根节点的path找最近的公共节点，path包含本身
"""