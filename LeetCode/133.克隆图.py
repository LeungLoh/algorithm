#
# @lc app=leetcode.cn id=133 lang=python3
#
# [133] 克隆图
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional


class Solution:
    def __init__(self) -> None:
        self.builed_node = {}
        self.visited = set()

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        new_root = Node(node.val)
        self.builed_node[node.val] = new_root
        self.dfs(node, new_root)
        return new_root

    def dfs(self, old_root: Optional['Node'], new_root: Optional['Node']):
        if len(old_root.neighbors) == 0:
            return
        if old_root.val in self.visited:
            return
        self.visited.add(old_root.val)
        _next = []
        for node in old_root.neighbors:
            if node.val not in self.builed_node:
                _node = Node(node.val)
                self.builed_node[node.val] = _node
            else:
                _node = self.builed_node[node.val]
            _next.append(_node)
        new_root.neighbors = _next

        for i in range(len(_next)):
            self.dfs(old_root.neighbors[i], new_root.neighbors[i])


# test = Solution()
# test.cloneGraph([[2, 4], [1, 3], [2, 4], [1, 3]])
# @lc code=end
