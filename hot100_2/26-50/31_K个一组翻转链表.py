from typing import Optional


class ListNode:
    def __init__(self,x:int):
        self.val = x
        self.next = None

class Solution:
    def kGroupReverse(self,head:Optional[ListNode],k:int) -> Optional[ListNode]:
        def reverseNodes(head_node:ListNode):
            # 如何翻转链表，需要加入dummy吗？先不加入吧
            pre = None
            p = head_node
            # q = head_node.next
            while p:
                q = p.next # 为什么要前置
                p.next = pre
                pre = p
                p = q
                # q = q.next  #会空
                # p走完之后pre就是头结点，那尾结点那就是送进来的头结点
            return pre,head_node

        dummy = ListNode(0)
        dummy.next = head
        pre_tail = dummy

        while True:
            cur_head = pre_tail
            cur_tail = cur_head
            for _ in range(k):
                cur_tail = cur_tail.next
                if cur_tail==None: # 如果最后一组不够k个，按顺序即不动
                    return dummy.next
            next_head = cur_tail.next
            cur_tail.next = None # 脱链，方便翻转
            cur_head = pre_tail.next

            new_head,new_tail = reverseNodes(cur_head)# 翻转链表

            pre_tail.next = new_head # 接前链
            new_tail.next = next_head # 接后链
            pre_tail = new_tail # 已处理的链表变为前链，更新标记的新尾部

        return dummy.next







"""
四个变量
前一个尾
当前头
当前尾
后一个头
我知道翻转链表，如何表示四个节点，翻转前的，翻转后的
翻转前的需要翻转的链表，尾结点断链，需要找一个记录节点。
头结点直接被前面的节点next，或者说在翻转链表中处理，第一个位置不翻转
            # 头插法，新结点的next指向pre的next，再pre.next = 新结点
            # cur的下一个也要有，移动的是下一个，因为第一个cur不用插进去
            # 固定第一个节点head不动，把后面的节点插入到head
            # dummy 1 2 3 4
            # dummy 2 1 3 4
            # dummy 3 2 1 4
            # dummy 4 3 2 1
"""