"""
输入一个字符串，打印出该字符串中字符的所有排列。

 

你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

 

示例:

输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]
"""


class Solution:
    def __init__(self) -> None:
        self.res = []

    def permutation(self, s: str) -> List[str]:
        if not s:
            return []
        self.dfs(list(s), "")
        return self.res

    def dfs(self, s, path):
        if not s:
            self.res.append(path)
            return
        visited = set()
        for index in range(len(s)):
            if s[index] in visited:
                continue
            visited.add(s[index])
            self.dfs(s[:index] + s[index + 1:], path + s[index])
