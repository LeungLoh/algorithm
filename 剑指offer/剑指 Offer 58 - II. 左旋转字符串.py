"""
字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。

示例 1：

输入: s = "abcdefg", k = 2
输出: "cdefgab"
示例 2：

输入: s = "lrloseumgh", k = 6
输出: "umghlrlose"
"""


class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        res = list(s)
        l = 0
        r = n - 1
        while l < r:
            res[l], res[r] = res[r], res[l]
            l += 1
            r -= 1
        l = n
        r = len(s) - 1
        while l < r:
            res[l], res[r] = res[r], res[l]
            l += 1
            r -= 1
        l = 0
        r = len(s) - 1
        while l < r:
            res[l], res[r] = res[r], res[l]
            l += 1
            r -= 1
        return "".join(res)
