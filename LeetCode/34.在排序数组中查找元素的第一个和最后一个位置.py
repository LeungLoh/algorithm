#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                break
            if nums[mid] > target:
                right -= 1
            else:
                left += 1
        if target == nums[mid]:
            left = mid
            right = mid
            while left > 0 and nums[left - 1] == target:
                left -= 1
            while right < len(nums) - 1 and nums[right + 1] == target:
                right += 1
            return [left, right]
        return [-1, -1]

# @lc code=end
