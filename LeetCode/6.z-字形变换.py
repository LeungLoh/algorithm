#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] N 字形变换
#
import math
# @lc code=start


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        length = numRows * 2 - 2
        m = [s[i:i + length] for i in range(0, len(s), length)]
        res = ""
        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                for item in m:
                    if len(item) > i:
                        res += item[i]
            else:
                for item in m:
                    temp1 = item[:numRows]
                    temp2 = item[numRows:][::-1]
                    temp2 = (numRows - len(temp2) - 1) * " " + temp2
                    if len(temp1) > i:
                        res += temp1[i]
                    if len(temp2) > i and temp2[i] != " ":
                        res += temp2[i]
        return res


test = Solution()
print(test.convert("ABCDE", 4))
# @lc code=end
