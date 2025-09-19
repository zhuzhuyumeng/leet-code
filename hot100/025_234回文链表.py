# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur = head
        ans = []
        while cur:
            ans.append(cur.val)
            cur = cur.next
        n = len(ans)
        left = 0
        right = n-1
        flag = True
        while left<right:
            if ans[left]!=ans[right]:
                flag=False
            left+=1
            right-=1
        return flag