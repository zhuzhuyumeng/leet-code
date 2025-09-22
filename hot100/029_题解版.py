# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def get_length(head:ListNode)->int:
            length = 0
            while (head):
                length += 1
                head = head.next
            return length

        dummy = ListNode(0,head)
        length = get_length(head)
        target = length-n+1
        cur = dummy
        for i in range(target):
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next

