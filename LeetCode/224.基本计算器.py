#
# @lc app=leetcode.cn id=224 lang=python3
#
# [224] 基本计算器
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        i = 0
        while i < len(s):
            c = s[i]
            if c == ")":
                temp = []
                while stack[-1] != "(":
                    temp.append(stack.pop())
                stack.pop()
                val = self._cap(temp[::-1])
                stack.append(val)
                i += 1
            elif c == " ":
                i += 1
            elif c in ["+", "-", "*", "/", "("]:
                stack.append(c)
                i += 1
            else:
                val = s[i]
                while i < len(s) - 1 and s[i + 1] not in ["+", "-", "*", "/", "(", ")", " "]:
                    i += 1
                    val += s[i]
                i += 1
                stack.append(int(val))
        return self._cap(stack)

    def _cap(self, s):
        i = 1 if s[0] == "-" else 0
        stack = []

        while i < len(s):
            if s[i] == "*":
                v1 = int(stack.pop())
                v2 = int(s[i + 1])
                stack.append(v1 * v2)
                i += 2
            elif s[i] == "/":
                v1 = int(stack.pop())
                v2 = int(s[i + 1])
                stack.append(v1 / v2)
                i += 2
            elif s[i] == "+" or s[i] == "-":
                stack.append(s[i])
                i += 1
            else:
                stack.append(s[i])
                i += 1

        i = 1
        res = stack[0] if s[0] != "-"else -stack[0]

        while i < len(stack):
            op = stack[i]
            v = int(stack[i + 1])
            if op == "+":
                res += v
            elif op == "-":
                res -= v
            i += 2
        return res


test = Solution()
# # print(test.calculate("1 + 1"))
# print(test.calculate("(1+(4+5+2)-3)+(6+8)"))
# print(test.calculate("1-(-2)"))
# print(test.calculate("-2+ 1"))
# @lc code=end
