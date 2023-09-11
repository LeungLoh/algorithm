#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        length = len(nums)
        nums = sorted(nums)
        for i in range(length - 3):
            for j in range(i + 1, length - 2):
                l = j + 1
                r = length - 1
                while l < r:
                    if nums[i] + nums[j] + nums[l] + nums[r] > target:
                        r -= 1
                    elif nums[i] + nums[j] + nums[l] + nums[r] < target:
                        l += 1
                    else:
                        res.add("{},{},{},{}".format(nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1
        return [list(map(int, item.split(",")))for item in res]

# @lc code=end
