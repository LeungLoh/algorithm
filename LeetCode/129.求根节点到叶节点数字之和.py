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

    def dfs(self, root, value):
        if not root:
            return
        v = value * 10 + root.val
        if root.left == None and root.right == None:
            self.res += v
        if root.left:
            self.dfs(root.left, v)
        if root.right:
            self.dfs(root.right, v)

# @lc code=end
