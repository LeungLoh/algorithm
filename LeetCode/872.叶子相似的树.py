#
# @lc app=leetcode.cn id=872 lang=python3
#
# [872] 叶子相似的树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.dfs(root1, 0) == self.dfs(root2, 0)

    def dfs(self, root, sums):
        if not root.left and not root.right:
            return sums * 10 + root.val
        if root.left:
            sums = self.dfs(root.left, sums)
        if root.right:
            sums = self.dfs(root.right, sums)
        return sums
# @lc code=end
