#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
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
        self.res = sys.maxsize
        self.pre = -1

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:
            return
        self.dfs(root.left)
        if self.pre != -1:
            self.res = min(self.res, root.val - self.pre)
        self.pre = root.val
        self.dfs(root.right)


# @lc code=end
