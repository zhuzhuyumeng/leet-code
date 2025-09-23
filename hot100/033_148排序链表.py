# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findmiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while fast and fast.next:  # 如果fast是最后一个，next就是空，如果是空，next超限
            pre = slow
            fast = fast.next.next
            slow = slow.next
        pre.next = None  # 中间位置前链断开
        print(slow)
        return slow

    def merge(self, head1: Optional[ListNode], head2: Optional[ListNode]):
        dummy = ListNode()
        cur = dummy
        while head1 and head2:
            if head1.val < head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next
        if head1:
            cur.next = head1
        if head2:
            cur.next = head2
        return dummy.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:  # 单个节点或为空
            return head
        head2 = self.findmiddle(head)
        head1 = self.sortList(head)
        head2 = self.sortList(head2)

        return self.merge(head1, head2)
"""
链表排序，比较一轮，该交换的交换，比较好多轮直到不交换。排序完毕
注意这里不能用head表示头部，因为一直在变化
[4,2,1,3]
[4,2],[1,3]
[2][3]
"""