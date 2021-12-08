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
        if s and not p:
            return False
        if len(p) > 1 and p[1] == '*':
            if not s:
                return self.isMatch(s, p[2:])
            if s[0] == p[0] or p[0] == '.':
                return self.isMatch(s, p[2:]) or self.isMatch(s[1:], p)
            else:
                return self.isMatch(s, p[2:])
        if s and (s[0] == p[0] or p[0] == '.'):
            return self.isMatch(s[1:], p[1:])
        else:
            return False

# @lc code=end
