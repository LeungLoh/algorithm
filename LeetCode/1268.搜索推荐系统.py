#
# @lc app=leetcode.cn id=1268 lang=python3
#
# [1268] 搜索推荐系统
#
from typing import *
from collections import *


# @lc code=start

class Tire:
    def __init__(self) -> None:
        self.child = [None] * 26
        self.isend = False
        self.word = ""

    def insert(self, word):
        root = self
        for c in word:
            index = ord(c) - ord('a')
            if not root.child[index]:
                root.child[index] = Tire()
            root = root.child[index]
        root.isend = True
        root.word = word

    def prefix(self, word):
        root = self
        for c in word:
            index = ord(c) - ord('a')
            if not root.child[index]:
                return []
            root = root.child[index]
        res = []
        self.dfs(root, res)
        return res

    def dfs(self, root, words):
        if not root:
            return words
        if root.isend:
            words.append(root.word)
        if len(words) == 3:
            return words

        for child in root.child:
            self.dfs(child, words)
            if len(words) == 3:
                break
        return words


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        tire = Tire()
        for word in products:
            tire.insert(word)
        res = []
        for i in range(1, len(searchWord) + 1):
            matched = tire.prefix(searchWord[:i])
            res.append(matched)
        return res


test = Solution()
test.suggestedProducts(["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse")
# @lc code=end
