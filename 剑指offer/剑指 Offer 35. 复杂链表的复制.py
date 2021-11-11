"""
请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。

输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]

"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        res = Node(0)
        m = {}
        node = head
        new_node = res
        while node:
            new_node.next = Node(node.val)
            new_node = new_node.next
            new_node.random = node.random
            m[node] = new_node
            node = node.next
        new_node = res
        while new_node:
            if new_node.random:
                new_node.random = m[new_node.random]
            new_node = new_node.next
        return res.next
