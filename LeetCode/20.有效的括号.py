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
            if item == "(" or item == "[" or item == "{":
                stack.append(item)
            elif item == ")":
                if not stack or stack[-1] != "(":
                    return False
                stack.pop()
            elif item == "}":
                if not stack or stack[-1] != "{":
                    return False
                stack.pop()
            elif item == "]":
                if not stack or stack[-1] != "[":
                    return False
                stack.pop()
        return True if not stack else False


test = Solution()
test.isValid("()")

# @lc code=end
