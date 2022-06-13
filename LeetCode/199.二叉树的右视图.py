#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
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
        self.view = []

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.dfs(root, 1)
        return self.view

    def dfs(self, root, depth):
        if not root:
            return
        if depth > len(self.view):
            self.view.append(root.val)
        self.dfs(root.right, depth + 1)
        self.dfs(root.left, depth + 1)
# @lc code=end
