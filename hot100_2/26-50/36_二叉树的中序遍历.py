from typing import Optional


class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inOrderTraversal(self,root:Optional[TreeNode])->list[int]:
        list = []
        self.inOrder(root,list)
        return list

    def inOrder(self,root:Optional[TreeNode]):
        if root is None:
            return
        self.inOrder(root.left)
        list.append(root.val)
        self.inOrder(root.right)
        return

class Solution2:
    def inOrderTraversal(self,root:Optional[TreeNode])->list[int]:
        stack,rst = [root],[]
        while stack:
            i = stack.pop()
            if isinstance(i,TreeNode):
                stack.extend([i.right,i.val,i.left]) #右子树先入栈，后出
            elif isinstance(i,int):
                rst.append(i)
        return rst

