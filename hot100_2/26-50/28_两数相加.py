from typing import Optional


class ListNode:
    def __init__(self,x:int):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoNumber(self,l1:Optional[ListNode],l2:Optional[ListNode]) -> Optional[ListNode]:
        pre = ListNode()
        cur = pre
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            sum = carry%10
            carry = carry/10
            cur.next = ListNode(sum)
            cur = cur.next
        return pre.next

"""
两个链表，不同形式
直接扫链表加上去，注意进位，为空当做0
"""