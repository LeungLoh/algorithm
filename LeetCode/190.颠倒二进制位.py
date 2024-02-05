#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start
# 00000010100101000001111010011100
# 00111001011110000010100101000000

# 11111111111111111111111111111101
# 10111111111111111111111111111111
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        bit = 32
        while bit:
            res <<= 1
            res += n & 1
            n >>= 1
            bit -= 1
        return res


# @lc code=end
