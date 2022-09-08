#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        s = []
        node = root
        while node:
            left = node.left
            right = node.right
            if right:
                s.append(right)
            node.left = None
            node.right = None
            if left:
                node.right = left
                node = left
            else:
                if s:
                    temp = s.pop()
                    node.right = temp
                    node = temp
                else:
                    node = None


# @lc code=end
