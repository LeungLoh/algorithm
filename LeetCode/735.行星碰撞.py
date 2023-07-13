#
# @lc app=leetcode.cn id=735 lang=python3
#
# [735] 行星碰撞
#
from typing import *
# @lc code=start


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for item in asteroids:
            d = False
            while stack and stack[-1] > 0 and item < 0:
                if abs(stack[-1]) < abs(item):
                    stack.pop()
                elif abs(stack[-1]) == abs(item):
                    stack.pop()
                    d = True
                    break
                elif abs(stack[-1]) > abs(item):
                    d = True
                    break
            if not d:
                stack.append(item)

        return stack


test = Solution()
test.asteroidCollision([5, 10, -5])
# @lc code=end
