# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

"""
一个链表逆序表示一个数字，遍历链表并求和，遇到>=10进位
最好还是通过node.next判断
        first = l1
        second = l2
        ans = 0
        beilv = 1
        while first and second:
            total = first.val + second.val
            ans = total * beilv + ans
            beilv = beilv * 10
            first = first.next
            second = second.next
        start = l1
        while first is not None:
            total = first.val
            ans = total * beilv + ans
            print(ans)
            print("-----------")
            print(first)
            beilv = beilv * 10
            first = first.next
            start = l1
        while second is not None:
            total = second.val
            ans = total * beilv + ans
            print(ans)
            print("-----------")
            beilv = beilv * 10
            second = second.next
            start = l2
        prex = start
        while ans:
            start.val = ans % 10
            print(ans)
            ans = int(ans / 10)
            if ans == 1:
                start.next = ListNode(1)
            start = start.next

        return prex
"""