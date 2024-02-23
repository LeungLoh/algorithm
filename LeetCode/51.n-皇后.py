#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.res = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.track(0, set(), set(), set(), [], n)
        return self.res

    def track(self, row, col, left, right, path, n):
        if row == n:
            self.res.append(path)
            return
        for i in range(n):
            if i in col or row - i in left or row + i in right:
                continue
            col.add(i)
            left.add(row - i)
            right.add(row + i)
            temp = ["."] * n
            temp[i] = "Q"
            self.track(row + 1, col, left, right, path + ["".join(temp)], n)
            col.remove(i)
            left.remove(row - i)
            right.remove(row + i)


# @lc code=end
