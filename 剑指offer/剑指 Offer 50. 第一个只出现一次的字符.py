"""
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例 1:

输入：s = "abaccdeff"
输出：'b'
示例 2:

输入：s = "" 
输出：' '
"""


class Solution:
    def firstUniqChar(self, s: str) -> str:
        m = {}
        for item in s:
            m[item] = m[item] + 1 if m[item] else 1
        for item in s:
            if m[item] == 1:
                return item
