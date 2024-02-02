#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
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
        self.res = 0
        self.k = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:
            return
        self.dfs(root.left)
        self.k -= 1
        if self.k == 0:
            self.res = root.val
            return
        self.dfs(root.right)

# @lc code=end
