from heapq import heapify, heappop, heappush
from typing import Optional


class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class Solution:
    def sortKList(self,lists:list[Optional[ListNode]])->Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        h = []
        heapify(h)# 堆化列表，小根堆
        # h = [head for head in lists if head]# 不能直接比较节点啊
        for i,head in enumerate(lists):
            if head:
                heappush(h,(head.val,i,head))

        while h:
            val,i,node = heappop(h)
            cur.next = node
            cur = node
            if node.next:
                heappush(h,(node.next.val,i,node.next))
        return dummy.next




"""
如何合并？不能是硬扫吧？
"""
