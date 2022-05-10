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
        for i in range(len(height)):
            while s and height[i] > height[s[-1]]:
                top = s.pop()
                if s:
                    left = s[-1]
                    res += (min(height[left], height[i]) - height[top]) * (i - left - 1)
            s.append(i)
        return res


# @lc code=end
