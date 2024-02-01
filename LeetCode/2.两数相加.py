#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1, num2 = 0, 0
        node1, node2 = l1, l2
        bit = 0
        while node1:
            num1 += node1.val * pow(10, bit)
            node1 = node1.next
            bit += 1
        bit = 0
        while node2:
            num2 += node2.val * pow(10, bit)
            node2 = node2.next
            bit += 1
        num = num1 + num2
        head = ListNode(0)
        node = head
        if num == 0:
            return head
        while num:
            val = num % 10
            node.next = ListNode(val)
            node = node.next
            num //= 10
        return head.next

# @lc code=end
