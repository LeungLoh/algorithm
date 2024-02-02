#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.dfs(p, q)

    def dfs(self, left, right):
        if not left and not right:
            return True
        if (left and not right) or (not left and right):
            return False
        if left.val != right.val:
            return False
        return self.dfs(left.left, right.left) and self.dfs(left.right, right.right)

# @lc code=end
