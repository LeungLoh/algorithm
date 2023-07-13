#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        _next = None
        pre = None
        node = head
        while node:
            _next = node.next
            node.next = pre
            pre = node
            node = _next
        return pre
# @lc code=end
