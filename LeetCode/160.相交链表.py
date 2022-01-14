#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        length1 = 0
        length2 = 0
        node1 = headA
        node2 = headB
        while node1:
            length1 += 1
            node1 = node1.next
        while node2:
            length2 += 1
            node2 = node2.next
        node1 = headA
        node2 = headB
        if length1 > length2:
            for _ in range(length1 - length2):
                node1 = node1.next
        else:
            for _ in range(length2 - length1):
                node2 = node2.next
        while node1 and node2:
            if node1 == node2:
                return node1
            node1 = node1.next
            node2 = node2.next
        return None


# @lc code=end
