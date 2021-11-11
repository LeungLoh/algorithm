#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        res = []
        for word in words:
            res.append(self.reverseword(list(word)))

        return " ".join(res)

    def reverseword(self, word):
        l = 0
        r = len(word) - 1
        while l < r:
            word[l], word[r] = word[r], word[l]
            l += 1
            r -= 1
        return "".join(word)
# @lc code=end
