#
# @lc app=leetcode.cn id=413 lang=python3
#
# [413] 等差数列划分
#

# @lc code=start
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        dp = [[0] * n for _ in range(n)]
        res = 0
        for i in range(n - 2):
            for j in range(i + 1, n):
                if j - i < 2:
                    continue
                if nums[j] - nums[j - 1] == nums[j - 1] - nums[j - 2]:
                    res += 1
                else:
                    break
        return res
# @lc code=end
