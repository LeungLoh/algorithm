#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    def check(self, nums):
        if len(nums) != len(set(nums)):
            return False
        for num in nums:
            if num < "1" or num > "9":
                return False
        return True

    def scan_row(self, board):
        for i in range(len(board)):
            temp = []
            for j in range(len(board[i])):
                if board[i][j] != ".":
                    temp.append(board[i][j])
            if not self.check(temp):
                return False
        return True

    def scan_col(self, board):
        for j in range(len(board[0])):
            temp = []
            for i in range(len(board)):
                if board[i][j] != ".":
                    temp.append(board[i][j])
            if not self.check(temp):
                return False
        return True

    def scan_matrix(self, board):
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                temp = []
                for k in range(3):
                    if board[i + k][j] != ".":
                        temp.append(board[i + k][j])
                    if board[i + k][j + 1] != ".":
                        temp.append(board[i + k][j + 1])
                    if board[i + k][j + 2] != ".":
                        temp.append(board[i + k][j + 2])
                if not self.check(temp):
                    return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.scan_row(board) and self.scan_col(board) and self.scan_matrix(board)

# @lc code=end
