# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from sys import prefix


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head: Optional[ListNode]):
            p = head.next
            pre = head
            while p is not None:
                q = p.next  # 遍历节点的后一个
                p.next = pre  # 修改下一个
                pre = p
                p = q
            # head.next.next =None # 第一个指向的应当是未给出的第一个，是的在循环后面补上了，这句不用
            last = head.next
            head.next = pre  # 头节点指向的是反过来的第一个
            return last  # 返回翻转链表的尾部

        dummy = ListNode(0, head)
        count = 0
        cur = dummy
        pre = cur
        while cur.next is not None:
            cur = cur.next
            count += 1
            if count % k == 0:
                nxt = cur.next  # 尾结点的下一个，下一个遍历区间第一个
                cur.next = None  # 当前节点断链
                pre = reverse(pre)  # 翻转已知链表，获得处理后尾节点
                print(pre)
                pre.next = nxt  # 给接上去
                cur = pre
        return dummy.next
# 注意在翻转之后cur的位置会变化，要给一个尾链位置
"""
        def reverse(pre: Optional[ListNode]):
            # 第一个head作为pre,他是一直不动的，只作为总链表的连接
            #
            last = pre.next
            cur = pre.next
            prev = None
            while cur is not None:
                nxt = cur.next # 遍历节点的后一个
                cur.next = prev # 修改下一个
                prev = cur
                cur = nxt
            # head.next.next =None # 第一个指向的应当是未给出的第一个，这个位置已经倒转了！！！
            pre.next = prev
            # 头节点指向的是反过来的第一个
            return last # 返回翻转链表的尾部
        dummy = ListNode(0,head)
        count = 0
        cur = dummy
        pre = dummy
        while cur.next is not None:
            cur = cur.next
            count+=1
            if count%k==0:
                # pre是第0个节点，翻转段的前一个，翻转后的最后一个
                nxt = cur.next
                cur.next= None
                pre = reverse(pre)
                pre.next = nxt # 给接上去
                cur = pre
        return dummy.next
"""










"""
通过一个专门的翻转链表的方法，在遍历的过程中把链表放进去
如果都从前一个的尾结点向后，dummy就有用了
[1,2,3,4,5]
0,1,3
"""