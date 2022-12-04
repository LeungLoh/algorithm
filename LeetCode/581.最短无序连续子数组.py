#
# @lc app=leetcode.cn id=581 lang=python3
#
# [581] 最短无序连续子数组
#

# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if (n <= 1):
            return 0
        maxv = nums[0]
        minv = nums[-1]
        right = 0
        left = n - 1
        for i in range(1, n):
            if nums[i] < maxv:
                right = i
            else:
                maxv = nums[i]
        for j in range(n - 2, -1, -1):
            if nums[j] > minv:
                left = j
            else:
                minv = nums[j]
        return right - left + 1 if right >= left else 0
# @lc code=end
