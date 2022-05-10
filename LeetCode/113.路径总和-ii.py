#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
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
        self.res = []

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.dfs(root, [], targetSum)
        return self.res

    def dfs(self, root, path, targetSum):
        if root is None:
            return
        if root.left == None and root.right == None:
            path.append(root.val)
            if sum(path) == targetSum:
                self.res.append(path)
            return
        self.dfs(root.left, path + [root.val], targetSum)
        self.dfs(root.right, path + [root.val], targetSum)

# @lc code=end
