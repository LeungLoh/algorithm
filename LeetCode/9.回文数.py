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
        num = x
        while num:
            num //= 10
            length += 1
        num = x

        for _ in range(length // 2):
            stack.append(num % 10)
            num //= 10
        if length % 2 != 0:
            num //= 10
        while num:
            if stack.pop() != num % 10:
                return False
            num //= 10
        return True


# @lc code=end
