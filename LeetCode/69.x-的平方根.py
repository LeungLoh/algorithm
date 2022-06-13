#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        for i in range(1, x):
            if i * i <= x and (i + 1) * (i + 1) > x:
                return i
# @lc code=end
