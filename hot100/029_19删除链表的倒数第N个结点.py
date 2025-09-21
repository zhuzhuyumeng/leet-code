# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 1
        fast = head
        while fast.next != None:
            fast = fast.next
            count += 1
        target = count - n + 1
        index = 1
        slow = head
        print("count:", count)
        print("target:", target)
        if target == 1:
            head = head.next
        else:
            while slow.next != None:
                pre = slow
                slow = slow.next
                index += 1
                if index == target:
                    print(pre)
                    if pre.next.next:
                        pre.next = pre.next.next
                    else:
                        pre.next = None
                    return head
                print(index)
        return head
        # 如果这个头没了怎么办