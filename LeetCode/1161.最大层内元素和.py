#
# @lc app=leetcode.cn id=1161 lang=python3
#
# [1161] 最大层内元素和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) -> None:
        self.max_sums = -sys.maxsize + 1
        self.max_level = 1

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.bfs([root], 1)
        return self.max_level

    def bfs(self, queue, depth):
        if not queue:
            return
        size = len(queue)
        sums = 0
        for _ in range(size):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            sums += node.val
        if sums > self.max_sums:
            self.max_sums = sums
            self.max_level = depth
        self.bfs(queue, depth + 1)

# @lc code=end
