#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N 叉树的层序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            size = len(queue)
            temp = []
            for _ in range(size):
                node = queue.pop(0)
                queue += node.children
                temp.append(node.val)
            res.append(temp)
        return res


# @lc code=end
