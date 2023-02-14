#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        p1 = head
        p2 = head
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                p1 = head
                while p1 != p2:
                    p1 = p1.next
                    p2 = p2.next
                return p1
        return None


# @lc code=end
