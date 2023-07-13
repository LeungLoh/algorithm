#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
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
        self.res = []

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        self.bfs([root])
        return self.res

    def bfs(self, queue):
        if not queue:
            return
        self.res.append(queue[-1].val)
        size = len(queue)
        for _ in range(size):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        self.bfs(queue)
# @lc code=end
