#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 翻转字符串里的单词
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return s
        s = s.strip().split(" ")
        res = []
        for word in s:
            if word:
                res.append(word)

        return " ".join(res[::-1])


# @lc code=end
