#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.res = []

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.dfs(nums, [])
        return self.res

    def dfs(self, nums, path, ):
        visited = set()
        if not nums:
            self.res.append(path)
            return
        for i in range(len(nums)):
            if nums[i] in visited:
                continue
            visited.add(nums[i])
            self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]])
# @lc code=end
