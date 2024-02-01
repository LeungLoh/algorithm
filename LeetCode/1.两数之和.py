#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, num in enumerate(nums):
            if m.get(num) != None:
                return [m[num], i]
            else:
                m[target - num] = i
        return [-1, -1]

# @lc code=end
