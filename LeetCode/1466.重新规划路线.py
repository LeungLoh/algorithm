#
# @lc app=leetcode.cn id=1466 lang=python3
#
# [1466] 重新规划路线
#

# @lc code=start
from typing import *


class Solution:
    def __init__(self) -> None:
        self.res = 0

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited = [0] * n
        self.dfs(connections, 0, visited)
        return self.res

    def dfs(self, connections, city, visited):
        for i in range(len(connections)):
            connection = connections[i]
            if connection[0] == city:
                if visited[connection[1]]:
                    continue
                visited[connection[1]] = 1
                connection[0], connection[1] = connection[1], connection[0]
                self.res += 1
                self.dfs(connections[:i] + connections[i + 1:], connection[0], visited)
            elif connection[1] == city:
                if visited[connection[0]]:
                    continue
                visited[connection[1]] = 1
                self.dfs(connections[:i] + connections[i + 1:], connection[0], visited)


test = Solution()
test.minReorder(6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]])
# @lc code=end
