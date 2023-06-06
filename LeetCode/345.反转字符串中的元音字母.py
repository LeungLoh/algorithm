#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set({"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"})
        s = list(s)
        p1 = 0
        p2 = len(s) - 1
        while p1 < p2:
            while p1 < p2 and s[p1] not in vowels:
                p1 += 1
            while p1 < p2 and s[p2] not in vowels:
                p2 -= 1
            if p1 < p2:
                s[p1], s[p2] = s[p2], s[p1]
                p1 += 1
                p2 -= 1

        return "".join(s)
# @lc code=end
