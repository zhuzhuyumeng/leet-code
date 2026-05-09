class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self,headA:ListNode,headB:ListNode) -> ListNode:
        a = headA
        b = headB
        while a is not b:
            if a:
                a = a.next
            else:
                a = headB
            if b:
                b = b.next
            else:
                b = headA
        return a

"""
两个链表一步一步动似乎并不能判断相交
都走一遍那不就肯定走到相交的地方了，
记交点前面的那段分别为a,b,交点之后一起的为c
A的长度为a+c，B的长度为b+c，A走到头后走B到交点则长度为a+c+b
B走到头后走A到交点则长度为b+c+a=a+c+b
"""
if __name__ == "__main__":
    intersectVal = 8
    listA = [4, 1, 8, 4, 5]
    listB = [5, 6, 1, 8, 4, 5]
    skipA = 2
    skipB = 3