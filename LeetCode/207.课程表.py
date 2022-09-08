#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        m = {}
        degrees = [0] * numCourses
        count = 0
        for v in prerequisites:
            degrees[v[0]] += 1
            if v[1] not in m.keys():
                m[v[1]] = [v[0]]
            else:
                m[v[1]].append(v[0])
        queue = [index for index in range(len(degrees)) if  degrees[index]== 0]
        while queue:
            cur = queue.pop(0)
            count += 1
            nextcourse = m.get(cur, [])
            if len(nextcourse) > 0:
                for item in nextcourse:
                    degrees[item] -= 1
                    if degrees[item] == 0:
                        queue.append(item)
        return count == numCourses


# @lc code=end
