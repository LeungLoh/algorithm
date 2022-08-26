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
            if item.isdigit():
                num = num * 10 + int(item)
            elif item == '[':
                stack.append([res, num])
                res, num = "", 0
            elif item == ']':
                temp = stack.pop()
                res = temp[0] + res * temp[1]
            else:
                res += item
        return res


# @lc code=end
