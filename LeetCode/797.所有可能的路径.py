#
# @lc app=leetcode.cn id=797 lang=python3
#
# [797] 所有可能的路径
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.res = []

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if not graph:
            return []
        n = len(graph)
        self.bfs(graph, 0, [0], n)
        return self.res

    def bfs(self, graph, node, path, n):
        if node == n - 1:
            self.res.append(path)
            return
        if not graph[node]:
            return
        for num in graph[node]:
            self.bfs(graph, num, path + [num], n)


# @lc code=end
