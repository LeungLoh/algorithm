#
# @lc app=leetcode.cn id=572 lang=python3
#
# [572] 另一棵树的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root and not subRoot:
            return True
        if not root:
            return False
        return self.dfs(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def dfs(self, rootA, rootB):
        if not rootA and not rootB:
            return True
        return rootA and rootB and rootA.val == rootB.val and self.dfs(rootA.left, rootB.left) and self.dfs(rootA.right, rootB.right)
# @lc code=end
