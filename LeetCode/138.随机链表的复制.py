#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 随机链表的复制
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new_head = Node(0)
        old_node = head
        new_node = new_head
        while old_node:
            node = Node(old_node.val)
            node.random = old_node.random
            old_node.random = node
            new_node.next = node

            new_node = new_node.next
            old_node = old_node.next
        old_node = head
        while old_node:
            new_node = old_node.random
            if new_node.random:
                new_node.random = new_node.random.random
            old_node = old_node.next
        return new_head.next


# @lc code=end
