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
        bit = 1
        res = ""
        while num:
            x = num % 10
            sign = self.m.get(bit)
            if x < 4:
                res = x * sign[0] + res
            elif x == 4:
                res = sign[0] + sign[1] + res
            elif x == 5:
                res = sign[1] + res
            elif x > 5 and x < 9:
                res = sign[1] + sign[0] * (x - 5) + res
            else:
                res = sign[0] + sign[2] + res
            num //= 10
            bit += 1
        return res


# @lc code=end
