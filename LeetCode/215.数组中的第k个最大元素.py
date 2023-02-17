#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not k or not nums:
            return -1
        if k > len(nums):
            return -1
        if k == 1 and len(nums) == 1:
            return nums[0]
        if len(nums) == 2 and (k == 1 or k == 2):
            if k == 1:
                return nums[0] if nums[0] > nums[1] else nums[1]
            if k == 2:
                return nums[0] if nums[0] < nums[1] else nums[1]
        p = self.parition(nums, 0, len(nums) - 1)
        if len(nums) - p == k:
            return nums[p]
        if len(nums) - p - 1 >= k:
            return self.findKthLargest(nums[p + 1:], k)
        else:
            return self.findKthLargest(nums[:p], k - (len(nums) - p))

    def parition(self, nums, l, r):
        pivot = nums[l]
        left = l
        right = r
        while left < right:
            while left < right and nums[right] >= pivot:
                right -= 1
            while left < right and nums[left] <= pivot:
                left += 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
        nums[l], nums[left] = nums[left], nums[l]
        return left

# @lc code=end
