#
# @lc app=leetcode.cn id=1679 lang=python3
#
# [1679] K 和数对的最大数目
#

# @lc code=start
class Solution:

    def maxOperations(self, nums: List[int], k: int) -> int:
        left = 0
        right = len(nums) - 1
        nums = sorted(nums)
        res = 0
        while left < right:
            if nums[left] + nums[right] > k:
                right -= 1
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                left += 1
                right -= 1
                res += 1
        return res
# @lc code=end
