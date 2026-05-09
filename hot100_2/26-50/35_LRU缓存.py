class ListNode:
    def __init__(self,key=0,value=0,next=None,pre=None):
        self.key = key
        self.value = value
        self.next = next
        self.pre = pre

class LRUCache:

    def __init__(self,capacity:int):
        self.capacity = capacity
        self.dummy = ListNode()
        self.dummy.next = self.dummy
        self.dummy.pre = self.dummy
        self.key_to_node = {}

    def get(self,key:int) ->int:
        if key not in self.key_to_node:
            return -1
        node = self.key_to_node[key]
        self.remove(node)
        self.put_front(node)
        return node.value

    def put(self,key:int,value:int):
        if key in self.key_to_node:
            # 找到原节点，修改value，抽出该节点，放到头部
            node = self.key_to_node[key]
            node.value = value
            self.remove(node)
            self.put_front(node)
            return

        node = ListNode(key,value)
        self.key_to_node[key] = node
        self.put_front(node)
        if len(self.key_to_node) > self.capacity:
            remove_node = self.dummy.pre
            self.key_to_node.pop(remove_node.key)
            self.remove(remove_node)

# 两边链一接就好了，但是如何消除这个点呢
    def remove(self,x:ListNode):
        x.pre.next = x.next
        x.next.pre = x.pre
# 放到链表头，先把新节点和链表接起来
    def put_front(self,x:ListNode):
        x.pre = self.dummy
        x.next = self.dummy.next
        x.next.pre = x
        x.pre.next = x


