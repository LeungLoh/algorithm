#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        cmp_s = ""
        for item in s:
            if ("a" <= item and item <= "z") or (item >= "0" and item <= "9"):
                cmp_s += item
            left = 0
            right = len(cmp_s) - 1
        while left <= right:
            if cmp_s[left] != cmp_s[right]:
                return False
            left += 1
            right -= 1
        return True
# @lc code=end
