# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        cnt = list()
        start = dummy
        while start.next != 0:
            cnt.append(start.next)
            start = start.next
        for i in range(n):
            cnt.pop()
        pre = cnt[n-1]
        pre.next = pre.next.next
        return dummy.next