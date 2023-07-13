#
# @lc app=leetcode.cn id=2130 lang=python3
#
# [2130] 链表最大孪生和
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        queue = []
        node = head
        while node:
            queue.append(node.val)
            node = node.next
        left = 0
        right = len(queue) - 1
        res = 0
        while left < right:
            res = max(res, queue[left] + queue[right])
            left += 1
            right -= 1
        return res


# @lc code=end
