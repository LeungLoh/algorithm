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
        return self.dfs(root,targetSum,0)

    def dfs(self,root,targetSum,total):
        if not root:
            return False
        if not root.left and not root.right:
            if total+root.val==targetSum:
                return True
            return False
        return self.dfs(root.left,targetSum,total+root.val) or self.dfs(root.right,targetSum,total+root.val)

# @lc code=end

