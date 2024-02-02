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
        nums = [item for item in range(1, n + 1)]
        self.dfs(nums, [], k)
        return self.res

    def dfs(self, nums, path, k):
        if not k:
            self.res.append(path)
            return
        for i, v in enumerate(nums):
            self.dfs(nums[i + 1:], path + [v], k - 1)

# @lc code=end
