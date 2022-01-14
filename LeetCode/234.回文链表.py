#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        length = 0
        node = head
        while node:
            node = node.next
            length += 1
        if length <= 1:
            return True
        node = head
        pre = None
        for _ in range(length // 2):
            pre = node
            node = node.next

        pre.next = None
        tail = self.reverse(node)
        p1 = head
        p2 = tail
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        if length % 2 == 0:
            res = False if p1 or p2 else True
        else:
            res = False if p1 or p2.next else True
        pre.next = self.reverse(tail)
        return res

    def reverse(self, head):
        pre = None
        next = None
        node = head
        while node:
            next = node.next
            node.next = pre
            pre = node
            node = next
        return pre

# @lc code=end
