class TrieNode:
    def __init__(self):
        self.childrenNode = [None]*26
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for ch in word:
            idx = ord(ch)-ord('a')
            # 这究竟是什么逻辑？第一个节点是存在root的childrenNode[ch]位置，同时创造一个新空结点，但是最后把它变成了isEnd=True
            if node.childrenNode[idx] is None: # 如果这个字符没有被创建过节点，新建一个
                node.childrenNode[idx] = TrieNode()
            node = node.childrenNode[idx]
        node.isEnd = True
        # 最后一个节点isEnd=True，childrenNode=[None]，因为没有子节点
        return None

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            idx = ord(ch)-ord('a')
            if node.childrenNode[idx] is None: # 这个字符不在树中
                return False
            node = node.childrenNode[idx] # 下一个
        # 找到末尾
        return node.isEnd


    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            idx = ord(ch)-ord('a')
            if node.childrenNode[idx] is None:
                return False
            node = node.childrenNode[idx]
        return True


trie = Trie()
print(trie.insert("apple"))
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
print(trie.insert("app"))
print(trie.search("app"))

"""
多个字符串，注意共享路径
插入，创建节点，把
"""