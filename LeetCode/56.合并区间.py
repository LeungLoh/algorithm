#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        starts = sorted([item[0]for item in intervals])
        ends = sorted([item[1]for item in intervals])
        i = 0
        j = 0
        while i < len(intervals):
            if i == len(intervals) - 1 or starts[i + 1] > ends[i]:
                res.append([starts[j], ends[i]])
                j = i + 1
            i += 1
        return res

# @lc code=end
