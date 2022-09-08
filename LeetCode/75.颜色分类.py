#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.sort(nums,0,len(nums)-1)

    def sort(self, nums, l, r):
        if l < r:
            p = self.parition(nums, l, r)
            self.sort(nums, l, p - 1)
            self.sort(nums, p + 1, r)

    def parition(self, nums, l, r):
        k = nums[l]

        while l < r:
            while l < r and nums[r] > k:
                r -= 1
            while l < r and nums[l] >= k:
                l += 1
            if l < r:
                nums[l], nums[r] = nums[r], nums[l]
        nums[l], nums[r] = nums[r], nums[l]
        return l
# @lc code=end
