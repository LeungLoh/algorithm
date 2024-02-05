#
# @lc app=leetcode.cn id=427 lang=python3
#
# [427] 建立四叉树
#

# @lc code=start
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

from typing import *


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        _sum = 0
        for item in grid:
            _sum += sum(item)
        if _sum == n * n:
            return Node(True, True, None, None, None, None)
        if _sum == 0:
            return Node(False, True, None, None, None, None)

        # grid 需要划分
        mid = n // 2
        if mid == 1:
            root = Node(True, False, None, None, None, None)
            root.topLeft = Node(True, True, None, None, None, None) if grid[0][0] else Node(False, True, None, None, None, None)
            root.topRight = Node(True, True, None, None, None, None) if grid[0][1] else Node(False, True, None, None, None, None)
            root.bottomLeft = Node(True, True, None, None, None, None) if grid[1][0] else Node(False, True, None, None, None, None)
            root.bottomRight = Node(True, True, None, None, None, None) if grid[1][1] else Node(False, True, None, None, None, None)
            return root
        root = Node(True, False, None, None, None, None)
        topleft = [item[:mid] for item in grid[:mid]]
        topright = [item[mid:] for item in grid[:mid]]
        buttomleft = [item[:mid] for item in grid[mid:]]
        buttomright = [item[mid:] for item in grid[mid:]]
        root.topLeft = self.construct(topleft)
        root.topRight = self.construct(topright)
        root.bottomLeft = self.construct(buttomleft)
        root.bottomRight = self.construct(buttomright)
        return root

# @lc code=end
