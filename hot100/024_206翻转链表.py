# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        pre = None
        while p:
            q = p.next
            p.next = pre
            pre = p
            p=q
        return pre
    # 头插法