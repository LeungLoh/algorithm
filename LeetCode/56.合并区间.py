#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        _intervals = sorted(intervals, key=lambda x: x[0])
        res = [_intervals[0]]
        for i in range(1, len(_intervals)):
            last = res[-1]
            if last[1] >= _intervals[i][0]:
                last[1] = max(last[1], _intervals[i][1])
                res.pop()
                res.append(last)
            else:
                res.append(_intervals[i])
        return res

# @lc code=end
