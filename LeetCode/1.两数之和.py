#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i in range(len(nums)):
            if m.get(nums[i]) == None:
                m[target - nums[i]] = i
            else:
                return [m[nums[i]], i]
        return [-1, -1]

# @lc code=end
