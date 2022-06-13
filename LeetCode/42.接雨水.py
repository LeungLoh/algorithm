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
<<<<<<< HEAD
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
=======
        for i in range(len(height)):
            while s and height[i] > height[s[-1]]:
                top = s.pop()
                if s:
                    left = s[-1]
                    res += (min(height[left], height[i]) - height[top]) * (i - left - 1)
            s.append(i)
>>>>>>> 256575617e3d6ae378b722569b3ce3e69c1a426c
        return res


# @lc code=end
