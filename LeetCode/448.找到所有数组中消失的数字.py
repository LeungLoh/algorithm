#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    #def findDisappearedNumbers(self, nums):
        i = 0
        while i < len(nums):
            if nums[i] - 1 == i or nums[i] == 0:
                i += 1
            elif nums[nums[i] - 1] == nums[i]:
                nums[i] = 0
                i += 1
            else:
                index = nums[i] - 1
                nums[i], nums[index] = nums[index], nums[i]
        res = []
        for i in range(len(nums)):
            if nums[i] == 0:
                res.append(i + 1)
        return res
# @lc code=end
