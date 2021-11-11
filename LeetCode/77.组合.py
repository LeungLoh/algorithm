#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.res = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n + 1)]
        self.dfs(nums, k, [])
        return self.res

    def dfs(self, nums, k, temp):
        if k == 0:
            self.res.append(temp)
            return
        for i in range(len(nums)):
            self.dfs(nums[i + 1:], k - 1, temp + [nums[i]])

# @lc code=end
