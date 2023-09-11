#
# @lc app=leetcode.cn id=630 lang=python3
#
# [630] 课程表 III
#

# @lc code=start
from queue import PriorityQueue
from typing import *


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses = sorted(courses, key=lambda x: x[1])
        end = 0
        q = PriorityQueue()
        for course in courses:
            if course[0] > course[1]:
                continue
            q.put(-course[0])
            end += course[0]
            if end > course[1]:
                max_duratyion = q.get()
                end += max_duratyion

        return q.qsize()


test = Solution()
test.scheduleCourse([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]])
# @lc code=end
