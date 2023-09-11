#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        stack = []
        length = 0
        n = x
        while n:
            n //= 10
            length += 1
        for _ in range(length // 2):
            stack.append(x % 10)
            x //= 10

        if length % 2 != 0:
            x //= 10

        for _ in range(length // 2):
            if stack.pop(-1) != x % 10:
                return False
            x //= 10
        return len(stack) == 0


# @lc code=end
