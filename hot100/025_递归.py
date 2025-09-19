# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.current_pointer = head
        def check(current_node=head):
            if current_node is not None:
                if not check(current_node.next):
                    return False
                if self.current_pointer.val!=current_node.val:
                    return False
                self.current_pointer = self.current_pointer.next
            return True
        return check()