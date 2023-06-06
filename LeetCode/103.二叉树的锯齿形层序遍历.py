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
        # if not root:
        #     return []
        # queue = [root]
        # flag = True
        # res = []
        # while queue:
        #     size = len(queue)
        #     temp = []
        #     for _ in range(size):
        #         node = queue.pop(0)
        #         temp.append(node.val)
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     if not flag:
        #         temp = temp[::-1]
        #     flag = not flag
        #     res.append(temp)
        # return res
        if not root:
            return []
        queue=[root]
        flag=True
        res=[]
        while queue:
            size=len(queue)
            temp=[]
            for _ in range(size):
                node=queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                temp.append(node.val)
            if flag:
                res.append(temp)
            else:
                res.append(temp[::-1])
        return res

# @lc code=end
