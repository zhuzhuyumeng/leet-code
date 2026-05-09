from typing import Optional


class ListNode:
    def __init__(self,x:int):
        self.val = x
        self.next = None

class Solution:
    def swapEachTwo(self,head:Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        dummy = ListNode()
        dummy.next = head
        pre = dummy
        cur = dummy
        while cur.next and cur.next.next:
            slow = cur.next
            fast = slow.next

            cur.next = fast
            slow.next = fast.next
            fast.next = slow

            cur = slow
        return dummy.next


