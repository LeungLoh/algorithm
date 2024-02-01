#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        pre = None
        node = head
        while node:
            start = node
            end = node
            for _ in range(k - 1):
                if end.next:
                    end = end.next
                else:
                    return head
            node = end.next
            end.next = None
            self.reverse(start, pre)
            if pre:
                pre.next = end
            else:
                head = end
            start.next = node
            pre = start

        return head

    def reverse(self, head, pre=None):
        node = head
        while node:
            _next = node.next
            node.next = pre
            pre = node
            node = _next
        return pre

# @lc code=end
