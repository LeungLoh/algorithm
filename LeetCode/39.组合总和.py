#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.res = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.dfs(candidates, [], 0, target)
        return self.res

    def dfs(self, candidates, path, sums, target):
        if sums == target:
            self.res.append(path)
            return
        if sums > target:
            return
        for i in range(len(candidates)):
            self.dfs(candidates[i:], path + [candidates[i]], sums + candidates[i], target)

# @lc code=end
