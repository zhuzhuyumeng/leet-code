class Trie:

    def __init__(self):
        self.children = [None]*26
        self.isEnd = False

    def insert(self, word: str) -> None:
        node = self
        for i in range(len(word)):
            ch = ord(word[i])-ord("a")
            if not node.children[ch]: # 如果子节点没有这个字母，就创建一个节点
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True # 一次只插入一个单词吗？

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node.isEnd and node is not None

    def searchPrefix(self,word:str) -> "Trie":
        node = self
        for i in range(len(word)):
            ch = ord(word[i]) - ord("a")
            if node.children[ch]:  # 存在这个字母
                node = node.children[ch]
            else:
                return None
        return node

    def startsWith(self, prefix: str) -> bool:
        node = self.searchPrefix(prefix)
        return node is not None

trie = Trie()
print(trie.insert("apple"))
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
print(trie.insert("app"))
print(trie.search("app"))

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)