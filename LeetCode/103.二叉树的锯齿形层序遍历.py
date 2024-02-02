#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from re import L


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        res = []
        is_reverse = True
        while queue:
            size = len(queue)
            temp = []
            for _ in range(size):
                if is_reverse:
                    node = queue.pop()
                    temp.append(node.val)
                    if node.left:
                        queue.insert(0, node.left)
                    if node.right:
                        queue.insert(0, node.right)
                else:
                    node = queue.pop(0)
                    temp.append(node.val)
                    if node.right:
                        queue.append(node.right)
                    if node.left:
                        queue.append(node.left)
                   
            res.append(temp)
            is_reverse = not is_reverse
        return res


# @lc code=end
