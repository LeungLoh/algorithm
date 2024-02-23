#
# @lc app=leetcode.cn id=210 lang=python3
#
# [210] 课程表 II
#
from collections import *
# @lc code=start


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course = [0] * numCourses
        graph = defaultdict(list)
        for v in prerequisites:
            course[v[0]] += 1
            graph[v[1]].append(v[0])
        queue = [i for i in range(len(course)) if course[i] == 0]
        res = []
        while queue:
            _class = queue.pop(0)
            res.append(_class)
            for item in graph[_class]:
                course[item] -= 1
                if course[item] == 0:
                    queue.append(item)
            numCourses -= 1
            if numCourses == 0:
                return res
        return []
# @lc code=end
