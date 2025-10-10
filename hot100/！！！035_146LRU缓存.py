class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
    def get(self, key: int) -> int:

    def put(self, key: int, value: int) -> None:

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
"""
第一个初始化是规定容量大小，
哈希表+链表，加入队尾，如果被查了就放链表尾，塞满了就扔掉链表头
为什么是双向链表，还循环上了

get
查询在不在，在节点内就要提到最新，先拉出来再插进去
不在return -1
put
查询在不在，在的话就要改值，不在的话就要新加，如果超了就要把最久未使用去除
"""