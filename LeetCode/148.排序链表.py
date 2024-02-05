#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        if length == 1:
            return head
        if length == 2:
            node1 = head
            node2 = head.next
            if node1.val > node2.val:
                node2.next = node1
                node1.next = None
                return node2
            else:
                return node1

        mid = length // 2
        mid_node = head
        for _ in range(mid - 1):
            mid_node = mid_node.next
        _next = mid_node.next
        mid_node.next = None
        left = self.sortList(head)
        right = self.sortList(_next)
        return self.merge(left, right)

    def merge(self, left, right):
        node_l = left
        node_r = right
        head = ListNode(0)
        node = head
        while node_l and node_r:
            if node_l.val < node_r.val:
                node.next = node_l
                node_l = node_l.next
            else:
                node.next = node_r
                node_r = node_r.next
            node = node.next
        if node_l:
            node.next = node_l
        if node_r:
            node.next = node_r
        return head.next


# @lc code=end
