#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def __init__(self) -> None:
#         self.res=[]
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         self.dfs(root)
#         return self.res
#     def dfs(self,root):
#         if not root:
#             return
#         self.dfs(root.left)
#         self.res.append(root.val)
#         self.dfs(root.right)

class Solution:

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        s = []

        node = root
        while node or s:
            while node:
                s.append(node)
                node = node.left
            if s:
                node = s.pop()
                res.append(node.val)
                node = node.right

        return res

# @lc code=end
