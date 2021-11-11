"""
统计一个数字在排序数组中出现的次数。
示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
示例 2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: 0
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = 0
        mid = 0
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + int((r - l) / 2)
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                res += 1
                break
        l = mid - 1
        r = mid + 1
        while l >= 0 and nums[l] == target:
            res += 1
            l -= 1
        while r <= len(nums) - 1 and nums[r] == target:
            res += 1
            r += 1
        return res
