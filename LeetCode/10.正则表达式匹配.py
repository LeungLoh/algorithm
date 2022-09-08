#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not s and not p:
            return True
        if not p:
            return False
        if len(p) > 1 and p[1] == "*":
            if not s:
                return self.isMatch(s, p[2:])
            elif s[0] == p[0] or p[0] == ".":
                return self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
            else:
                return self.isMatch(s, p[2:])
        elif s and (s[0] == p[0] or p[0] == "."):
            return self.isMatch(s[1:], p[1:])
        else:
            return False

# @lc code=end
