#
# @lc app=leetcode.cn id=617 lang=python3
#
# [617] 合并二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        res = self.dfs(root1, root2)
        return res

    def dfs(self, root1, root2):
        if root1 == None and root2:
            return root2
        elif root2 == None:
            return root1

        root1.val += root2.val
        root1.left = self.dfs(root1.left, root2.left)
        root1.right = self.dfs(root1.right, root2.right)
        return root1


# @lc code=end
