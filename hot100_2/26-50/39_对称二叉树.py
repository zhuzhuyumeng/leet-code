from collections import deque
from tabnanny import check
from typing import Optional


class TreeNode:
    def __init__(self,val=0,left=None,right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self,root:Optional[TreeNode])->bool:
        if root is None:
            return True
        queue = deque([(root.left,root.right)])

        while queue:
            left,right = queue.popleft()
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            queue.append((left.left,right.right))
            queue.append((left.right, right.left))
        return True

class Solution2:
    def isSymmetric(self,root:Optional[TreeNode])->bool:
        def InOrder(left:Optional[TreeNode],right:Optional[TreeNode])->bool:
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            outSame = InOrder(left.left,right.right)
            inSame = InOrder(left.right,right.left)
            isSame = outSame and inSame
            return isSame

        if root is None:
            return True
        return InOrder(root.left,root.right)



"""
除了层序和迭代，我想不出其他方法
层序判断是否为偶数
直接整层判断是否回文呗，不可以，这样没有空节点的判断
要成对的判断
"""