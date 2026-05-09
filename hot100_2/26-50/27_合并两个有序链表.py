class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self,list1:ListNode,list2:ListNode) -> ListNode:
        p = list1
        q = list2
        cur = ListNode(-1)
        cur_first = cur
        while p and q:
            if p.val < q.val:
                pnext = p.next
                cur.next = p
                p = pnext
                cur = cur.next
            else:
                qnext = q.next
                cur.next = q
                q = qnext
                cur = cur.next
        if p:# 如果A还在，我怎么知道现在链表的尾结点是哪个啊？
            cur.next = p
        if q:
            cur.next = q
        return cur_first.next




if __name__ == "__main__":
    intersectVal = 8
    listA = [4, 1, 8, 4, 5]
    listB = [5, 6, 1, 8, 4, 5]
    skipA = 2
    skipB = 3