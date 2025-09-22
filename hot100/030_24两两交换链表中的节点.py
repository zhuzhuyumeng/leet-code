# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        cur = dummy
        while cur.next!=None and cur.next.next!=None:
            print(cur)
            first = cur.next
            second = cur.next.next

            first.next = second.next
            second.next = first
            cur.next = second
            cur = first

        return dummy.next


"""
直接加入一个哨兵节点，后面有两个就交换，然后移动到交换后的第二个
"""