from typing import Optional


class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next


class Solution:
    def sortNodeList(self,head:Optional[ListNode])->Optional[ListNode]:
        def sortList(head: Optional[ListNode]) -> Optional[ListNode]:
            if not head or not head.next:
                return head
            slow = head
            fast = head.next

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            mid = slow.next # 后链的头结点
            slow.next = None # 前链脱链

            l1 = sortList(head)
            l2 = sortList(mid)

            return mergeList(l1,l2)

        def mergeList(l1:Optional[ListNode],l2:Optional[ListNode]):
            dummy = ListNode(0)
            tail = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            tail.next = l1 if l1 else l2

            return dummy.next # 返回排序后的头节点

        return sortList(head)


"""
排序，升序从小到大
链表如何处理，不可能全指针然后排序后再接回去吧
"""