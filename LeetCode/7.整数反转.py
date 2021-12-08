#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        flag = False

        if x < 0:
            x = -x
            flag = True
        while x:
            res = res * 10 + x % 10
            x //= 10
        res = -res if flag else res

        return res if res < pow(2, 31) and res >= -pow(2, 31) else 0
# @lc code=end
