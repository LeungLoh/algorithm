#
# @lc app=leetcode.cn id=400 lang=python3
#
# [400] 第 N 位数字
#

# @lc code=start
class Solution:
    def findNthDigit(self, n: int) -> int:
        if n < 10:
            return n
        k = 1
        length = 0
        cnt = 9
        while n > length + cnt * k:
            length += cnt * k
            cnt *= 10
            k += 1

        num = pow(10, k - 1) + (n - length - 1) // k
        index = (n - length - 1) % k
        return int(str(num)[index])

# @lc code=end
