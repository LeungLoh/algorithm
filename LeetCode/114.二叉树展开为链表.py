#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        self.dfs(root)

    def dfs(self, root):
        start, end = root, root
        left = root.left
        right = root.right
        if left:
            lstart, lend = self.dfs(left)
            end.left = None
            end.right = lstart
            end = lend
        if right:
            rstart, rend = self.dfs(right)
            end.left = None
            end.right = rstart
            end = rend
        return start, end

# @lc code=end
