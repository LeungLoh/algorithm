#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.res = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.dfs(nums, [])
        return self.res

    def dfs(self, nums, path):
        self.res.append(path)
        if not nums:
            return
        for i in range(len(nums)):
            self.dfs(nums[i + 1:], path + [nums[i]])

# @lc code=end
