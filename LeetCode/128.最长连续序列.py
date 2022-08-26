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
        for num in nums:
            if num not in m:
                left = m.get(num - 1, 0)
                right = m.get(num + 1, 0)
                length = left + right + 1

                res = max(res, length)

                m[num] = length
                m[num - left] = length
                m[num + right] = length
        return res
# @lc code=end
