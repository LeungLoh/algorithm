#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        s = []
        res=0
        for i in len(height):
            if not s:
                s.append(i)
            elif height[i] < height[s[-1]]:
                s.append(i)
            else:
                length = 0
                tmp=0
                while s and  height[i]>=height[s[-1]]:
                    tmp+=height[s.pop()]
                    length += 1
                if s:
                    


# @lc code=end
