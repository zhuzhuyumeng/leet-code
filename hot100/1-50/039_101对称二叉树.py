# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 递归法
        if root is None:
            return True
        stack = []
        stack.append(root.left)
        stack.append(root.right)
        while stack:
            right = stack.pop()
            left = stack.pop()
            if left==None and right!=None:
                return False
            elif left!=None and right==None:
                return False
            elif left==None and right==None:
                continue
            elif left.val != right.val:
                return False
            # 成双成对
            stack.append(left.left)
            stack.append(right.right)
            stack.append(left.right)
            stack.append(right.left)
        return True

        # 迭代法
        # def isOrnot(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        #     if left == None and right != None:  # 空节点不对称
        #         return False
        #     elif left != None and right == None:
        #         return False
        #     elif left == None and right == None:  # 全为空,提到前面，因为后面会空值
        #         return True
        #     elif left.val != right.val:  # 值不对称
        #         return False
        #     # 左右节点一致，且有值，进行下一阶段判断
        #     outSame = isOrnot(left.left, right.right)
        #     inSame = isOrnot(left.right, right.left)
        #     isSame = outSame and inSame
        #     return isSame
        #
        # if root is None:
        #     return True
        # flag = isOrnot(root.left, root.right)
        # return flag