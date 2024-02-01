#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#
from typing import *
# @lc code=start


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            intervals.append(newInterval)
            return intervals
        res = []
        if intervals[0][0] <= newInterval[0]:
            res.append(intervals[0])
            inserted = False
            i = 1
        else:
            res.append(newInterval)
            inserted = True
            i = 0

        while i < len(intervals):
            last = res[-1]
            if not inserted:
                if last[0] <= newInterval[0] and intervals[i][0] > newInterval[0]:
                    inserted = True
                    if last[1] >= newInterval[0]:
                        last[1] = max(last[1], newInterval[1])
                        res.pop()
                        res.append(last)
                    else:
                        res.append(newInterval)
                else:
                    res.append(intervals[i])
                    i += 1
            else:
                if last[1] >= intervals[i][0]:
                    last[1] = max(last[1], intervals[i][1])
                    res.pop()
                    res.append(last)
                else:
                    res.append(intervals[i])
                i += 1
        if not inserted:
            last = res[-1]
            if last[1] >= newInterval[0]:
                last[1] = max(last[1], newInterval[1])
                res.pop()
                res.append(last)
            else:
                res.append(newInterval)

        return res


# test = Solution()
# print(test.insert([[0, 5], [9, 12]], [7, 16]))

# @lc code=end
