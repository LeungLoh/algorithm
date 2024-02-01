#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#
from typing import *
# @lc code=start


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(v1 + v2)
            elif token == "-":
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(v2 - v1)
            elif token == "*":
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(v1 * v2)
            elif token == "/":
                v1 = stack.pop()
                v2 = stack.pop()
                stack.append(int(v2 / v1))
            else:
                stack.append(int(token))
        return stack[-1]


test = Solution()
test.evalRPN(["4", "13", "5", "/", "+"])
# @lc code=end
