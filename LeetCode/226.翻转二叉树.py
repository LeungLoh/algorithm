#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.dfs(root)
        return root

    def dfs(self, root):
        if not root:
            return
        left = root.left
        right = root.right
        root.left = right
        root.right = left
        self.dfs(root.left)
        self.dfs(root.right)


# @lc code=end
