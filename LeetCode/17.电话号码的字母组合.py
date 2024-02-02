#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.m = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        self.res = []

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return self.res
        self.dfs(digits, "")
        return self.res

    def dfs(self, digits, path):
        if not digits:
            self.res.append(path)
            return
        for c in self.m[digits[0]]:
            self.dfs(digits[1:], path + c)

# @lc code=end
