#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        node1 = l1
        node2 = l2
        head = ListNode(0)
        p = head
        while node1 and node2:
            if node1.val < node2.val:
                node = node1
                node1 = node1.next
            else:
                node = node2
                node2 = node2.next
            node.next = None
            p.next = node
            p = p.next
        if node1:
            p.next = node1
        elif node2:
            p.next = node2
        return head.next

# @lc code=end
