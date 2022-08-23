#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                break
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
        if l > r:
            return [-1, -1]
        p1 = mid
        p2 = mid
        while p1 > 0 and nums[p1 - 1] == target:
            p1 -= 1
        while p2 < len(nums) - 1 and nums[p2 + 1] == target:
            p2 += 1
        return [p1, p2]

# @lc code=end
