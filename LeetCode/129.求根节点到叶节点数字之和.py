#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根节点到叶节点数字之和
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

    def sumNumbers(self, root: TreeNode) -> int:
        self.dfs(root, 0)
        return self.res

    def dfs(self, root, v):
        if not root:
            return
        if not root.left and not root.right:
            self.res += v * 10 + root.val
            return
        self.dfs(root.left, v * 10 + root.val)
        self.dfs(root.right, v * 10 + root.val)

# @lc code=end
