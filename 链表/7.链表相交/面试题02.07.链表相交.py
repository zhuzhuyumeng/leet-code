# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cura = headA
        curb = headB
        if headA is None or headB is None:
            return None
        while cura is not curb:
            if cura is not None:
                cura = cura.next
            else:
                cura = headB
            if curb is not None:
                curb = curb.next
            else:
                curb = headA
        return cura
        # 分开来移动，不要一起移动
        #
        # if headA is None or headB is None:
        #     return None
        # while headA!=headB:
        #     if headA.next is not None or headB.next is not None:
        #         headA = headA.next
        #         headB = headB.next
        #     else:
        #         headA = headB
        #         headB = headA
        # return headA
        #

"""
哈希哦
"""