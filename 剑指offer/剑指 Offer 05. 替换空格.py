"""
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

 

示例 1：

输入：s = "We are happy."
输出："We%20are%20happy."
"""


class Solution:
    def replaceSpace(self, s: str) -> str:
        res = []
        for item in s[::-1]:
            if item == " ":
                res.insert(0, "%20")
            else:
                res.insert(0, item)
        return "".join(res)
