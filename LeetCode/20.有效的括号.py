#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for item in s:
            if item == "(" or item == "{" or item == "[":
                stack.append(item)
            elif stack and ((item == ")" and  stack[-1] == "(") or
                            (item == "}" and  stack[-1] == "{")or
                            (item == "]" and  stack[-1] == "[")
            ):
               
                    stack.pop()
            else:
                return False          
        return True if not stack else False

# @lc code=end
