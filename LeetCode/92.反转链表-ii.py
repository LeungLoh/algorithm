#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        p1 = head
        p2 = head
        pre = None
        _next = head.next
        for _ in range(left - 1):
            pre = p1
            p1 = p1.next
        for _ in range(right - 1):
            p2 = p2.next
            _next = p2.next
        p2.next = None
        n_head = self.reverse(p1, pre)
        if pre:
            pre.next = n_head
            p1.next = _next
            return head
        else:
            p1.next = _next
            return p2

    def reverse(self, head, pre=None):
        node = head
        while node:
            _next = node.next
            node.next = pre
            pre = node
            node = _next
        return pre


# @lc code=end
