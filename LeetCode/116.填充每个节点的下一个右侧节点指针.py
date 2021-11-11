#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        self.dfs(root)
        return root

    def dfs(self, root):
        if not root or not root.left:
            return
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        self.dfs(root.left)
        self.dfs(root.right)


# @lc code=end
