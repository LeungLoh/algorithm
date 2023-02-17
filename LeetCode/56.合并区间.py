#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals = sorted(intervals, key=lambda x: x[0])
        index = 0
        start = intervals[0][0]
        end = intervals[0][1]
        res = []
        while index < len(intervals):
            if index == len(intervals) - 1:
                res.append([start, end])
            elif end < intervals[index + 1][0]:
                res.append([start, end])
                start = intervals[index + 1][0]
                end = intervals[index + 1][1]
            else:
                end = max(intervals[index + 1][1], end)
            index += 1
        return res


# @lc code=end
