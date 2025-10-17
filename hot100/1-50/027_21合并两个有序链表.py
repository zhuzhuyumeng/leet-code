# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        first = list1
        second = list2
        if not list1:
            return second
        if not list2:
            return first
        if first.val<=second.val:
            new = first
            first = first.next
        else:
            new = second
            second = second.next
        star = new
        while first and second:
            if first.val<=second.val:
                new.next =first
                first = first.next
            else:
                new.next = second
                second = second.next
            new = new.next
        if first is not None:
            new.next = first
        else:
            new.next = second
        return star

# 链表题还是要注意空的