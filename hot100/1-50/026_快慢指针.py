# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:




"""
a是头结点到圆起点的距离
b是圆的周长
fast走2k，slow走k
快指针多走了n圈 k=nb，slow走了nb步
慢走a步到达环入口
相遇的地方是不知道的，但是入口肯定是a+nb以圆周长为界的
周长可以通过走一圈来测量，2k = a +2nb
"""