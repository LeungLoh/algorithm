#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start
class Solution:
    def __init__(self):
        self.m = {
            1: ['I', 'V', 'X'],
            2: ['X', 'L', 'C'],
            3: ['C', 'D', 'M'],
            4: ['M']
        }

    def intToRoman(self, num: int) -> str:
        res = ""
        index = 1
        while num:
            bit = num % 10
            sign = self.m[index]
            if bit < 4:
                s = sign[0] * bit
            elif bit == 4:
                s = sign[0] + sign[1]
            elif bit == 5:
                s = sign[1]
            elif bit > 5 and bit < 9:
                s = sign[1] + sign[0] * (bit - 5)
            else:
                s = sign[0] + sign[-1]
            num //= 10
            index += 1
            res = s + res
        return res


# @lc code=end
