#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        n = len(nums)
        for i in range(n - 2):
            if nums[i] > 0:
                break
            l = i + 1
            r = n - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    res.append("{},{},{}".format(nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
        res = list(set(res))
        return [[int(num) for num in item.split(",")]for item in res]


# @lc code=end
