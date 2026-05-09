from typing import Optional


class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def isPardmoe(self,head:Optional[ListNode]) -> bool:
        p = head
        ans = []
        while p:
            ans.append(p.val)
            p = p.next
        n = len(ans)
        left = 0
        right = n-1
        while left<right:
            if ans[left] != ans[right]:
                return False
            left+=1
            right-=1

        return True
"""
只给一个头，如何解决从尾部遍历
"""


if __name__ == "__main__":
    intersectVal = 8
    listA = [4, 1, 8, 4, 5]
    listB = [5, 6, 1, 8, 4, 5]
    skipA = 2
    skipB = 3