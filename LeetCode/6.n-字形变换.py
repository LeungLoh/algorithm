#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] N 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        length = 2 * numRows - 2
        rows = [s[i:i + length] for i in range(0, len(s), length)]
        down, up = [], []
        for item in rows:
            if len(item) == length:
                down.append(item[:numRows])
                up.append(" " + item[numRows:][::-1] + " ")
            elif len(item) <= numRows:
                down.append(item + " " * (numRows - len(item)))
                up.append(" " * numRows)
            elif numRows < len(item) < length:
                down.append(item[:numRows])
                up.append(" " * (length - len(item) + 1) + item[numRows:][::-1] + " ")

        x = 0
        res = ""
        while x < numRows:
            for i in range(len(down)):
                if down[i][x] != " ":
                    res += down[i][x]
                if up[i][x] != " ":
                    res += up[i][x]
            x += 1
        return res


# test = Solution()
# print(test.convert("ABCDE", 4))
# @lc code=end
