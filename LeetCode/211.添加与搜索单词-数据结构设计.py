#
# @lc app=leetcode.cn id=211 lang=python3
#
# [211] 添加与搜索单词 - 数据结构设计
#

# @lc code=start
class WordDictionary:

    def __init__(self):
        self.child = [None] * 26
        self.isend = False

    def addWord(self, word: str) -> None:
        node = self
        for c in word:
            index = ord(c) - ord('a')
            if not node.child[index]:
                node.child[index] = WordDictionary()
            node = node.child[index]
        node.isend = True

    def search(self, word: str, node=None) -> bool:
        if node == None:
            node = self
        for i, c in enumerate(word):
            if c == ".":
                for item in node.child:
                    if item and self.search(word[i + 1:], item):
                        return True
                return False
            else:
                index = ord(c) - ord("a")
                if not node.child[index]:
                    return False
                node = node.child[index]
        return node.isend


wordDictionary = WordDictionary()
wordDictionary.addWord("a")
wordDictionary.addWord("aa")
# wordDictionary.search(".")
# wordDictionary.search("a")
wordDictionary.search("a.")
# wordDictionary.search("pad")
# wordDictionary.search("bad")
# wordDictionary.search(".ad")
# wordDictionary.search("b..")
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end
