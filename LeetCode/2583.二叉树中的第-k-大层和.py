
#
# @lc app=leetcode.cn id=2583 lang=python3
#
# [2583] 二叉树中的第 K 大层和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        queue = [root]
        res = []
        while queue:
            size = len(queue)
            ans = 0
            for _ in range(size):
                node = queue.pop(0)
                ans += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            heapq.heappush(res, -ans)
        while res and k - 1:
            heapq.heappop(res)
            k -= 1

        return -res[0] if res else -1

# @lc code=end
