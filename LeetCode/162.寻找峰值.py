#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#
import sys
# @lc code=start


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums.insert(0, -sys.maxsize)
        nums.append(sys.maxsize)
        left = 1
        right = len(nums) - 2
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return mid - 1
            if nums[mid + 1] > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return left - 1

# @lc code=end
