#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
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
        if not root:
            return root
        self.dfs([root])
        return root

    def dfs(self, queue):
        if not queue:
            return
        root = queue.pop(0)

        if root.left:
            queue.append(root.left)
            if root.right:
                root.left.next = root.right
            else:
                node = root.next
                while node and not node.left and not node.right:
                    node = node.next
                if node and node.left:
                    root.left.next = node.left
                elif node and node.right:
                    root.left.next = node.right

        if root.right:
            queue.append(root.right)
            node = root.next
            while node and not node.left and not node.right:
                node = node.next
            if node and node.left:
                root.right.next = node.left
            elif node and node.right:
                root.right.next = node.right

        self.dfs(queue)

# @lc code=end
