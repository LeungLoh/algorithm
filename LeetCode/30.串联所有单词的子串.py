#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#

# @lc code=start
from typing import *


class Solution:

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        step = len(words[0])
        length = len(words[0]) * len(words)
        res = []
        words_map = DefaultDict(int)
        for word in words:
            words_map[word] += 1
        for i in range(0, len(s) - length + 1):
            temp = s[i:i + length]
            paths = [temp[i:i + step] for i in range(0, length, step)]
            visited = DefaultDict(int)
            for word in paths:
                if word in words:
                    visited[word] += 1
                else:
                    break

            if len(visited) != len(words_map):
                continue

            check = True
            for k, v in visited.items():
                if words_map.get(k, 0) != v:
                    check = False
                    break
            if check:
                res.append(i)
        return res


test = Solution()
# print(test.findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo", "barr", "wing", "ding", "wing"]))
# @lc code=end
