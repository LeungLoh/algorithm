#
# @lc app=leetcode.cn id=784 lang=python3
#
# [784] 字母大小写全排列
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.res = []

    def letterCasePermutation(self, s: str) -> List[str]:
        self.dfs(list(s), 0, [])
        return self.res

    def dfs(self, s, index, temp):
        if len(temp) == len(s):
            self.res.append("".join(temp))
            return
        if s[index] >= 'a' and s[index] <= 'z':
            self.dfs(s, index + 1, temp + [s[index]])
            self.dfs(s, index + 1, temp + [s[index].upper()])
        elif s[index] >= 'A' and s[index] <= 'Z':
            self.dfs(s, index + 1, temp + [s[index]])
            self.dfs(s, index + 1, temp + [s[index].lower()])
        else:
            self.dfs(s, index + 1, temp + [s[index]])

# @lc code=end
