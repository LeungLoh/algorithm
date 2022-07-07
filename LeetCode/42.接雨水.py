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
                index = s.pop()
                if s:
                    l = s[-1]
                    r = i
                    res += (r - l - 1) * (min(height[l], height[r]) - height[index])
            s.append(i)
        return res
       

# @lc code=end
