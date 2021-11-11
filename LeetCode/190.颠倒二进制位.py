#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        i = 32
        while i:
            res <<= 1
            res += n & 1
            n >>= 1
            i -= 1
        return res

# @lc code=end
