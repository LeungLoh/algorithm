#
# @lc app=leetcode.cn id=1372 lang=python3
#
# [1372] 二叉树中的最长交错路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) -> None:
        self.res = -1

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.dfs(root, -1, "left")
        self.dfs(root, -1, "right")
        return self.res

    def dfs(self, root, size, direct):
        if not root:
            self.res = max(self.res, size)
            return
        if direct == "left":
            self.dfs(root.left, size + 1, "right")
            self.dfs(root.right, 0, "left")
        else:
            self.dfs(root.right, size + 1, "left")
            self.dfs(root.left, 0, "right")

# @lc code=end
