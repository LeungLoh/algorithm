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
        p1 = headA
        p2 = headB
        length1 = 0
        length2 = 0
        while p1:
            length1 += 1
            p1 = p1.next
        while p2:
            length2 += 1
            p2 = p2.next
        p1 = headA
        p2 = headB
        if length1 > length2:
            for _ in range(length1 - length2):
                p1 = p1.next
        else:
            for _ in range(length2 - length1):
                p2 = p2.next
        while p1 and p2:
            if p1 == p2:
                return p1
            p1 = p1.next
            p2 = p2.next
        return None

# @lc code=end
