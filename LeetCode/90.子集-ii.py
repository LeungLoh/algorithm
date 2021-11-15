#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.res = []

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.dfs(nums, [])
        return self.res

    def dfs(self, nums, path):
        visited = set()
        self.res.append(path)
        if not nums:
            return
        for i in range(len(nums)):
            if nums[i] in visited:
                continue
            visited.add(nums[i])
            self.dfs(nums[i + 1:], path + [nums[i]])
# @lc code=end
