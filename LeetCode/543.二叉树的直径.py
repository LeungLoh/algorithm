#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
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
        self.res = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root.left and not root.right:
            return 0
        left, right = 0, 0
        if root.left:
            left = self.dfs(root.left) + 1
        if root.right:
            right = self.dfs(root.right) + 1
        self.res = max(self.res, left + right)
        return max(left, right)
# @lc code=end
