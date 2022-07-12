#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        m = len(num1) - 1
        n = len(num2) - 1
        res = ""
        flag = False
        while m >= 0 and n >= 0:
            cur = int(num1[m]) + int(num2[n])
            cur = cur + 1 if flag else cur
            if cur >= 10:
                flag = True
                cur = cur % 10
            else:
                flag = False
            res = str(cur) + res
            m -= 1
            n -= 1
        while m >= 0:
            cur = int(num1[m]) + 1 if flag else int(num1[m])
            if cur >= 10:
                flag = True
                cur = cur % 10
            else:
                flag = False
            res = str(cur) + res
            m -= 1
        while n >= 0:
            cur = int(num2[n]) + 1 if flag else int(num2[n])
            if cur >= 10:
                flag = True
                cur = cur % 10
            else:
                flag = False
            res = str(cur) + res
            n -= 1
        if flag:
            res = "1" + res
        return res
# @lc code=end
