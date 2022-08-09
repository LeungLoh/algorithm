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
        pre = None
        next = None
        node = head
        for _ in range(left - 1):
            pre = node
            node = node.next
        for _ in range(right - left):
            node = node.next
        next = node.next
        node.next = None
        if pre:
            node = pre.next
            pre.next = None
            start, end = self.reverse(node)
            pre.next = start
        else:
            start, end = self.reverse(head)
            head = start
        end.next = next
        return head

    def reverse(self, head):
        pre = None
        next = None
        node = head
        while node:
            next = node.next
            node.next = pre
            pre = node
            node = next
        return pre, head


# @lc code=end
