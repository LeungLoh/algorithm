#
# @lc app=leetcode.cn id=1732 lang=python3
#
# [1732] 找到最高海拔
#

# @lc code=start
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        front = 0
        for height in gain:
            front += height
            res = max(res, front)
        return res
# @lc code=end
