class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self,head:ListNode) -> ListNode:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                break
        if fast is None or fast.next is None:
            return False
        else:
            return True
        fast = head
        while slow!=fast:
            slow = slow.next
            fast = fast.next
        return True



if __name__ == "__main__":
    intersectVal = 8
    listA = [4, 1, 8, 4, 5]
    listB = [5, 6, 1, 8, 4, 5]
    skipA = 2
    skipB = 3