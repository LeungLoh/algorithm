#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
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
#     def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         self.dfs(root)
#         return self.res

#     def dfs(self,root):
#         if not root:
#             return
#         self.dfs(root.left)
#         self.dfs(root.right)
#         self.res.append(root.val)

class Solution:

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        s = [root]
        res = []
        while s:
            node = s.pop()
            res.append(node.val)
            if node.left:
                s.append(node.left)
            if node.right:
                s.append(node.right)

        return res[::-1]
# @lc code=end
