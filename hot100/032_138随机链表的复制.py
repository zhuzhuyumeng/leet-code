"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        cur = head
        while cur: # 复制链表
            cur.next = Node(cur.val,cur.next)
            cur = cur.next.next

        cur = head
        while cur: # 复制链表+random
            if cur.random:
                cur.next.random = cur.random.next # 这个.next就是指向的复制出来的节点
            cur = cur.next.next

        cur = head.next
        while cur.next:
            cur.next = cur.next.next
            cur = cur.next

        return head.next



"""
好聪明的解法，交错链表，创建一个新结点与原节点一致放到当前节点的后面，再次遍历random只需要指向对应的复制节点
再次遍历，复制节点形成一条链
"""