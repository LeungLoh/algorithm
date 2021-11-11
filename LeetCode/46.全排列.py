#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.res = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.dfs(nums, [])
        return self.res

    def dfs(self, nums, temp):
        if not nums:
            self.res.append(temp)
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], temp + [nums[i]])

# @lc code=end
