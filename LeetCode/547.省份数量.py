#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 省份数量
#

# @lc code=start
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        isvisit = [0] * n
        res = 0
        for i in range(n):
            if isvisit[i] == 0:
                res += 1
                isvisit[i] == 1
                self.dfs(isConnected, isvisit, i, n)
        return res

    def dfs(self, isConnected, isvisit, i, n):
        for j in range(n):
            if isConnected[i][j] == 1 and isvisit[j] == 0:
                isvisit[j] = 1
                self.dfs(isConnected, isvisit, j, n)
# @lc code=end
