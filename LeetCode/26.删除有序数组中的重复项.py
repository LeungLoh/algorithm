#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 2:
            return length
        index = 0
        for cur in range(1, length):
            if nums[index] != nums[cur]:
                nums[index + 1] = nums[cur]
                index += 1
        return index + 1
# @lc code=end
