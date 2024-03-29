#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, -sys.maxsize, sys.maxsize)

    def dfs(self, root, left, right):
        if not root:
            return True
        if root.val <= left or root.val >= right:
            return False
        return self.dfs(root.left, left, root.val) and self.dfs(root.right, root.val, right)


# @lc code=end
