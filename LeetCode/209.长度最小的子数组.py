#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        sums = 0
        res = sys.maxsize
        while r < len(nums):
            while r < len(nums) and sums < target:
                sums += nums[r]
                r += 1
            while l <= r and sums >= target:
                res = min(res, r - l)
                sums -= nums[l]
                l += 1
        return res if res != sys.maxsize else 0

# @lc code=end
