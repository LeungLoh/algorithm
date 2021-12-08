#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
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
        self.res = -sys.maxsize - 1

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:
            return 0
        left = max(self.dfs(root.left), 0)
        right = max(self.dfs(root.right), 0)
        self.res = max(self.res, root.val + left + right)
        return max(left, right) + root.val


# @lc code=end
