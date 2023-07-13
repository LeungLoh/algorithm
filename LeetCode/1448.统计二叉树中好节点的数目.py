#
# @lc app=leetcode.cn id=1448 lang=python3
#
# [1448] 统计二叉树中好节点的数目
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0

    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return self.res
        self.dfs(root, root.val)
        return self.res

    def dfs(self, root, _max):
        if not root:
            return
        if root.val >= _max:
            self.res += 1
            _max = root.val
        self.dfs(root.left, _max)
        self.dfs(root.right, _max)
# @lc code=end
