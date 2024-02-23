#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start
class Trie:

    def __init__(self):
        self.child = [None] * 26
        self.isend = False

    def insert(self, word: str) -> None:
        node = self
        for c in word:
            index = ord(c) - ord('a')
            if not node.child[index]:
                node.child[index] = Trie()
            node = node.child[index]
        node.isend = True

    def search(self, word: str) -> bool:
        node = self
        for c in word:
            index = ord(c) - ord('a')
            if not node.child[index]:
                return False
            node = node.child[index]
        if node.isend:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        node = self
        for c in prefix:
            index = ord(c) - ord('a')
            if not node.child[index]:
                return False
            node = node.child[index]

        return True


test = Trie()
test.insert("apple")
# test.search("apple")
# test.search("app")
# test.startsWith("startswith")
test.insert("app")
test.search("app")

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end
