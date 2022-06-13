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
        count = 1
        while p1.next and p2.next and p2.next.next:
            p1 = p1.next
            p2 = p2.next.next
            count += 1
            if p1 == p2:
                p3 = head
                while p1 != p3:
                    p1 = p1.next
                    p3 = p3.next
                return p1
        return None


# @lc code=end
