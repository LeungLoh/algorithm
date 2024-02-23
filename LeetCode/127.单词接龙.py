#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#
import string
# @lc code=start
from typing import *


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        chars = set()
        for c in beginWord:
            chars.add(c)
        for c in endWord:
            chars.add(c)
        for item in wordList:
            for c in item:
                chars.add(c)

        queue = [beginWord]
        step = 1
        visited = set()
        visited.add(beginWord)
        while queue:
            size = len(queue)
            for _ in range(size):
                cur = queue.pop(0)
                if cur == endWord:
                    return step
                for word in wordList:
                    if word in visited:
                        continue
                    if not self.cantransform(cur, word):
                        continue
                    queue.append(word)
                    visited.add(word)

            step += 1
        return 0

    def cantransform(self, src, dst):
        count = 0
        for i, v in enumerate(src):
            if v != dst[i]:
                count += 1
                if count > 1:
                    return False
        return count == 1


test = Solution()
test.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
# @lc code=end
