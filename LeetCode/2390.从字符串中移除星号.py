#
# @lc app=leetcode.cn id=2390 lang=python3
#
# [2390] 从字符串中移除星号
#

# @lc code=start
class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        for item in s:
            if item !="*":
                stack.append(item)
            elif stack:
                stack.pop()
        return "".join(stack)

# @lc code=end

