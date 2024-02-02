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
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.dfs(root, 0)

    def dfs(self, root, total):
        if not root.left and not root.right:
            return total + root.val
        res = 0
        if root.left:
            res += self.dfs(root.left, (total + root.val) * 10)
        if root.right:
            res += self.dfs(root.right, (total + root.val) * 10)
        return res


# @lc code=end
