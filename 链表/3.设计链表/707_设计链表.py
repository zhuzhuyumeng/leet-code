class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.dummy_head = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        # 直接获取第一个节点，然后往后数，比size大就再见
        if index<0 or index >= self.size:
            return -1
        cur = self.dummy_head.next
        for _ in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.dummy_head.next
        self.dummy_head.next = new_node
        self.size +=1


    def addAtTail(self, val: int) -> None:
        cur = self.dummy_head
        for _ in range(self.size):
            cur = cur.next
        new_node = ListNode(val)
        new_node.next = cur.next
        cur.next = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index<0 or index>self.size:
            return
        cur = self.dummy_head
        for _ in range(index):
            cur = cur.next
        new_node = ListNode(val)
        new_node.next = cur.next
        cur.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index<0 or index>=self.size:
            return
        cur = self.dummy_head.next
        pre = self.dummy_head
        for _ in range(index):
            pre = cur
            cur = cur.next
        pre.next = cur.next
        self.size -= 1
        # 为0的时候cur应当在第0位，不能在dummy

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)