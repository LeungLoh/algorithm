#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next or not head.next.next:
            return False

        p1 = head
        p2 = head.next.next
        while p2 and p2.next:
            if p1 == p2:
                return True
            p1 = p1.next
            p2 = p2.next.next
        return False

# @lc code=end
