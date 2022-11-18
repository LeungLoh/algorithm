#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dpf = [1] * n
        dpe = [1] * n
        for i in range(1, n):
            dpf[i] = dpf[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            dpe[i] = dpe[i + 1] * nums[i + 1]
        res = []
        for i in range(n):
            res.append(dpf[i] * dpe[i])
        return res
# @lc code=end
