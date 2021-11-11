#
# @lc app=leetcode.cn id=844 lang=python3
#
# [844] 比较含退格的字符串
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        p1 = len(s) - 1
        p2 = len(t) - 1
        skips = 0
        skipt = 0
        while p1 >= 0 or p2 >= 0:
            while p1 >= 0:
                if s[p1] == '#':
                    skips += 1
                    p1 -= 1
                elif skips > 0:
                    skips -= 1
                    p1 -= 1
                else:
                    break
            while p2 >= 0:
                if t[p2] == '#':
                    skipt += 1
                    p2 -= 1
                elif skipt > 0:
                    skipt -= 1
                    p2 -= 1
                else:
                    break
            if p1 >= 0 and p2 >= 0:
                if s[p1] != t[p2]:
                    return False
            elif p1 >= 0 or p2 >= 0:
                return False
            p1 -= 1
            p2 -= 1
        return True


# @lc code=end
