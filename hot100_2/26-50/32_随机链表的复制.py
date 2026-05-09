from typing import Optional


class Node:
    def __init__(self,val:int ,next:'Node'=None ,random:'Node'=None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def randomCopyList(self,head:Optional[Node])-> Optional[Node]:
        if head is None:
            return None
        cur = head
        while cur:
            cur.next = Node(cur.val,cur.next)
            # 创建新节点复制当前节点的值，并入链
            cur = cur.next.next

        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            # 复制节点的random，为当前节点random的复制节点
            cur = cur.next.next

        cur = head.next
        while cur.next:# 下一个原节点还在
            cur.next = cur.next.next
            cur = cur.next
            # 复制节点接下一个复制节点，记得移动
        return head.next
"""
节点未创建，random如何指向
一个节点创建一个新节点，random重新扫，再给。
"""