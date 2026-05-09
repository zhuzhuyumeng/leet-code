class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def reverseNodeList(self,head:ListNode) -> ListNode:
        pre = None
        p = head
        while p:
            q = p.next
            p.next = pre
            pre = p
            p = q

        return 0


if __name__ == "__main__":
    intersectVal = 8
    listA = [4, 1, 8, 4, 5]
    listB = [5, 6, 1, 8, 4, 5]
    skipA = 2
    skipB = 3