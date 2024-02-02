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
        self.dfs(candidates, target, [])
        return self.res

    def dfs(self, candidates, target, path):
        if target == 0:
            self.res.append(path)
            return
        if target < 0:
            return
        for i, v in enumerate(candidates):
            self.dfs(candidates[i:], target - v, path + [v])


# @lc code=end
