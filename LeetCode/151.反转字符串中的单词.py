#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 翻转字符串里的单词
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        while "" in s:
            s.remove("")
        return " ".join(s[::-1])

# @lc code=end
