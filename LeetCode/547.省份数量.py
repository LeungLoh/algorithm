#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 省份数量
#

# @lc code=start
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [0] * n
        res = 0
        for i in range(n):
            if visited[i] == 0:
                res += 1
                visited[i] == 1
                self.dfs(isConnected, visited, i, n)
        return res

    def dfs(self, isConnected, visited, i, n):
        for j in range(n):
            if isConnected[i][j] == 1 and visited[j] == 0:
                visited[j] = 1
                self.dfs(isConnected, visited, j, n)

# @lc code=end
