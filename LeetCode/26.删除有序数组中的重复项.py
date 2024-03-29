#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        for i, v in enumerate(nums):
            if index == 0:
                nums[index] = v
                index += 1
            elif v != nums[index - 1]:
                nums[index] = v
                index += 1
        return index
# @lc code=end
