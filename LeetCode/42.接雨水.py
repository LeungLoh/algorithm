#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        s = []
        res = 0
        length = len(height)
        for i in range(length):
            if not s:
                s.append(i)
            elif height[i] < s[-1]:
                s.append(i)
            else:
                temp = height[s[-1]]
                for index in range(s[-1] + 1, i):
                    res += temp - height[index]
                s.pop()
        return res


# @lc code=end
