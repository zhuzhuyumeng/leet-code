"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if root is None:
            return res
        stack = [root]
        while stack:
            temp = []
            val = []
            for i in range(len(stack)):
                val.append(stack[i].val)
                for j in range(len(stack[i].children)):
                    if stack[i].children[j]:
                        temp.append(stack[i].children[j])
            res.append(val)
            stack = temp
        return res