#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return self.dfs(root, 0, targetSum)

    def dfs(self, root, total, targetSum):
        if not root.left and not root.right:
            return True if total + root.val == targetSum else False
        if root.left:
            if self.dfs(root.left, total + root.val, targetSum):
                return True
        if root.right:
            if self.dfs(root.right, total + root.val, targetSum):
                return True
        return False
# @lc code=end
