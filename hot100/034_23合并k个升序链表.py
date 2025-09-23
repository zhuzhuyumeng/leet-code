# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
ListNode.__lt__ = lambda a,b: a.val < b.val
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        h = [head for head in lists if head]
        heapify(h)
        while h:
            node = heappop(h)
            cur.next = node
            cur = cur.next
            if node.next:
                heappush(h, node.next)
        return dummy.next
"""
一个一个比较吗

"""