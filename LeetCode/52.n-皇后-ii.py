#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N 皇后 II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        return self.track(0, set(), set(), set(), n)

    def track(self, row, col, left, right, n):
        res = 0
        if row == n:
            return 1
        for i in range(n):
            if i in col or row - i in left or row + i in right:
                continue
            col.add(i)
            left.add(row - i)
            right.add(row + i)
            res += self.track(row + 1, col, left, right, n)
            col.remove(i)
            left.remove(row - i)
            right.remove(row + i)
        return res


# @lc code=end
