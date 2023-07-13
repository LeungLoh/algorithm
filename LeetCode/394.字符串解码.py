#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#

# @lc code=start


from curses.ascii import isdigit


class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        res = ""
        num = 0
        for item in s:
            if isdigit(item):
                num = num * 10 + int(item)
            elif item == "[":
                stack.append((res, num))
                num = 0
                res = ""
            elif item == "]":
                temp = stack.pop()
                res = temp[0] + temp[1] * res
            else:
                res += item
        return res


# @lc code=end
