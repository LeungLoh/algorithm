#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)

    def dfs(self, root):
        if not root:
            return 0
        resa = root.val
        if root.left:
            resa += self.dfs(root.left.left) + self.dfs(root.left.right)
        if root.right:
            resa += self.dfs(root.right.left) + self.dfs(root.right.right)

        resb = self.dfs(root.left) + self.dfs(root.right)

        return max(resa, resb)

# @lc code=end
