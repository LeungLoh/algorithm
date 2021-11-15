#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.res = []

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.dfs(candidates, [], 0, target)
        return self.res

    def dfs(self, candidates, path, sums, target):
        visited=set()
        if sums == target:
            self.res.append(path)
            return
        if sums > target:
            return
        for i in range(len(candidates)):
            if candidates[i] in visited:
                continue
            visited.add(candidates[i])
            self.dfs(candidates[i + 1:], path + [candidates[i]], sums + candidates[i], target)
# @lc code=end
