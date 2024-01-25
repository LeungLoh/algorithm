#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除有序数组中的重复项 II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        for i, v in enumerate(nums):
            if index < 2:
                nums[index] = v
                index += 1
            elif v != nums[index - 1] or v != nums[index - 2]:
                nums[index] = v
                index += 1
        return index
# @lc code=end
