#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#
from typing import *
# @lc code=start


class Solution:
    def __init__(self) -> None:
        self.res = []

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [i for i in range(1, 10)]
        self.dfs(nums, k, n, [])
        return self.res

    def dfs(self, nums, k, n, path):
        if k == 0:
            if n == 0:
                self.res.append(path)
            return
        for i in range(len(nums)):
            self.dfs(nums[i + 1:], k - 1, n - nums[i], path + [nums[i]])


test = Solution()
test.combinationSum3(3, 7)
# @lc code=end
