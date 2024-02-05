#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        flag = True
        for i in range(len(digits) - 1, -1, -1):
            if not flag:
                break
            num = digits[i] + 1
            if num >= 10:
                digits[i] = num % 10
                flag = True
            else:
                digits[i] = num
                flag = False
        if flag:
            digits.insert(0, 1)
        return digits

# @lc code=end
