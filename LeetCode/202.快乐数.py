#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set()
        while n not in nums:
            nums.add(n)
            ans = 0
            while n:
                ans += pow(n % 10, 2)
                n //= 10
            if ans == 1:
                return True
            n = ans
        return False

# @lc code=end
