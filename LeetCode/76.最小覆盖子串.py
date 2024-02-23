#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
from collections import *
# @lc code=start


class Solution:

    def minWindow(self, s: str, t: str) -> str:
        m = Counter(t)
        left = 0
        right = 0
        res = ""
        while right <= len(s):
            if [v for v in m.values() if v > 0]:
                if right < len(s) and m.get(s[right]) != None:
                    m[s[right]] -= 1
                right += 1
            else:
                if not res or len(res) > right - left:
                    res = s[left:right]
                if m.get(s[left]) != None:
                    m[s[left]] += 1
                left += 1
        return res


# test = Solution()
# print(test.minWindow("ADOBECODEBANC", "ABC"))
# @lc code=end
