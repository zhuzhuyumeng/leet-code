# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        slow = head
        fast = head
        while fast!=None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                index1 = slow
                index2 = head
                while index1 != index2:
                    index1 = index1.next
                    index2 = index2.next
                return index1
        return None
"""
快2k，慢k
设环前为x，相遇点为y，相遇点到环起点为z
慢必定跑不完，只走了一圈不到环，因为快一直在追慢
慢（x+y）=k
2（x+y）=x+y+n(y+z)走了n圈环
x = n(y+z) - y
x = (n-1)(y+z)+z

"""
