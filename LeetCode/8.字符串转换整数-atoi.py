#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        flag = False
        if s[0] == '-' or s[0] == '+':
            flag = True if s[0] == '-' else False
            s = s[1:]

        res = 0
        for item in s:
            if item not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                break
            res = res * 10 + int(item)
            if flag and res > pow(2, 31):
                res = pow(2, 31)
                break
            elif not flag and res > pow(2, 31) - 1:
                res = pow(2, 31) - 1
                break

        return -res if flag else res
# @lc code=end
