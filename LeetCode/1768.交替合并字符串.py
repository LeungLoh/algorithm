#
# @lc app=leetcode.cn id=1768 lang=python3
#
# [1768] 交替合并字符串
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        flag = True
        res = ""
        while i < len(word1) and j < len(word2):
            if flag:
                res += word1[i]
                i += 1
            else:
                res += word2[j]
                j += 1
            flag = not flag
        if i < len(word1):
            res += word1[i:]
        if j < len(word2):
            res += word2[j:]
        return res
# @lc code=end
