#
# @lc app=leetcode.cn id=399 lang=python3
#
# [399] 除法求值
#
from collections import defaultdict
from typing import *
# @lc code=start


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for i in range(len(equations)):
            a, b = equations[i]
            graph[a][b] = values[i]
            graph[b][a] = 1.0 / values[i]
        res = []
        for query in queries:
            if query[0] not in graph or query[1] not in graph:
                res.append(-1)
            else:
                res.append(self.dfs(graph, query[0], query[1], 1, set()))
        return res

    def dfs(self, graph, start, end, value, visited):
        path = graph[start]
        if path.get(end):
            return value * path[end]
        for k, v in path.items():
            if k in visited:
                continue
            visited.add(k)
            res = self.dfs(graph, k, end, value * v, visited)
            if res != -1:
                return res
        return -1


# test = Solution()
# print(test.calcEquation([["x1", "x2"], ["x2", "x3"], ["x3", "x4"], ["x4", "x5"]], [3.0, 4.0, 5.0, 6.0],
#       [["x1", "x5"], ["x5", "x2"], ["x2", "x4"], ["x2", "x2"], ["x2", "x9"], ["x9", "x9"]]))

# @lc code=end
