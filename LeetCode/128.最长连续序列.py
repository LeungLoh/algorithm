#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = {}
        res = 0
        for i, v in enumerate(nums):
            if v not in m:
                left = m.get(v - 1, 0)
                right = m.get(v + 1, 0)
                length = right + left + 1
                res = max(res, length)
                m[v] = length
                m[v - left] = length
                m[v + right] = length
        return res

# @lc code=end
