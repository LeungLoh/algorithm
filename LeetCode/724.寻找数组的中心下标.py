#
# @lc app=leetcode.cn id=724 lang=python3
#
# [724] 寻找数组的中心下标
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        dps = [0]
        dpe = [0]
        for i in range(len(nums) - 1):
            dps.append(nums[i] + dps[-1])
        for i in range(len(nums) - 1, 0, -1):
            dpe.append(nums[i] + dpe[-1])
        dpe = dpe[::-1]

        for i in range(len(nums)):
            if dps[i] == dpe[i]:
                return i
        return -1
# @lc code=end
