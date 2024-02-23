#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start
from collections import *

from typing import *


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        courses = [0] * numCourses
        for v in prerequisites:
            graph[v[1]].append(v[0])
            courses[v[0]] += 1
        queue = [i for i in range(len(courses)) if courses[i] == 0]
        while queue:
            _class = queue.pop(0)
            for item in graph[_class]:
                courses[item] -= 1
                if courses[item] == 0:
                    queue.append(item)
            numCourses -= 1
            if numCourses == 0:
                return True
        return False


test = Solution()
print(test.canFinish(3, [[1, 0], [1, 2], [0, 1]]))
# @lc code=end
