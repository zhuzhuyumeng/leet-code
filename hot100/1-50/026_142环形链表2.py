# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        hash = set()
        while head:
            if head in hash:
                return head
            hash.add(head)
            head = head.next
        return None
    def detectCycle2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        fast = head
        slow = head
        while fast!=None:
            slow = slow.next
            if fast.next == None:
                return None
            fast = fast.next.next
            if fast==slow:
                ptr = head
                while ptr!=slow:
                    ptr = ptr.next
                    slow = slow.next
                return ptr
        return None