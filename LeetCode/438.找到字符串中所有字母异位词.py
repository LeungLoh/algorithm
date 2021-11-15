#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window = len(p)
        l = 0
        r = window
        res = []
        while r <= len(s):
            if self.check(s[l:r], p):
                res.append(l)
                while r < len(s) and s[r] == s[l]:
                    l += 1
                    r += 1
                    res.append(l)

            l += 1
            r += 1
        return res

    def check(self, a, b):
        a = "".join(sorted(a))
        b = "".join(sorted(b))
        return a == b

# @lc code=end
