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

    def dfs(self, nums, path):
        if not nums:
            self.res.append(path)
            return
        for i, v in enumerate(nums):
            self.dfs(nums[:i] + nums[i + 1:], path + [v])

# @lc code=end
