from typing import Optional


class ListNode:
    def __init__(self,x:int):
        self.val = x
        self.next = None

class Solution:
    def deleteNNode(self,head:Optional[ListNode],n:int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        stack = list()
        count = -1
        cur = dummy
        while cur:
            count += 1
            stack.append(cur)
            cur = cur.next
        # 栈加载

        for i in range(n):
            cur = stack.pop()
        pre = stack.pop()
        pre.next = cur.next
        cur.next = None
        return dummy.next
