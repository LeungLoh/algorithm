#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.res = set()

    def generateParenthesis(self, n: int) -> List[str]:
        self.dfs(n, 0, "")
        return list(self.res)

    def dfs(self, left, right, path):
        if left == 0:
            path += ")" * right
            self.res.add(path)
            return
        if right:
            self.dfs(left, right - 1, path + ")")
        self.dfs(left - 1, right + 1, path + "(")

# @lc code=end
