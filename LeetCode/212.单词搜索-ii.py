#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#
from typing import *
# @lc code=start


class Tire:
    def __init__(self) -> None:
        self.child = [None] * 26
        self.end = False
        self.word = ""

    def insert(self, word):
        node = self
        for c in word:
            index = ord(c) - ord("a")
            if not node.child[index]:
                node.child[index] = Tire()
            node = node.child[index]
        node.end = True
        node.word = word

    def search(self, word):
        node = self
        for c in word:
            index = ord(c) - ord("a")
            if not node.child[index]:
                return False
            node = node.child[index]
        node.end = True


class Solution:
    def __init__(self) -> None:
        self.res = set()

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        tire = Tire()
        for word in words:
            tire.insert(word)

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, tire)
        return list(self.res)

    def dfs(self, board, i, j, tire: Tire):
        if tire.end:
            self.res.add(tire.word)
        
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] == -1:
            return

        c = board[i][j]

        index = ord(c) - ord("a")
        if not tire.child[index]:
            return
        board[i][j] = -1
        self.dfs(board, i - 1, j, tire.child[index])
        self.dfs(board, i + 1, j, tire.child[index])
        self.dfs(board, i, j - 1, tire.child[index])
        self.dfs(board, i, j + 1, tire.child[index])
        board[i][j] = c


test = Solution()
print(test.findWords([["a"]], ["a"]))
# @lc code=end
