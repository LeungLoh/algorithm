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
        node1=headA
        node2=headB
        length1=0
        length2=0
        while node1:
            node1=node1.next
            length1+=1
        while node2:
            node2=node2.next
            length2+=1
        node1=headA
        node2=headB
        if length1>length2:
            for i in range(length1-length2):
                node1=node1.next
        elif length2>length1:
            for i in range(length2-length1):
                node2=node2.next
        while node1 and node2:
            if node1==node2:
                return node1
            node1=node1.next
            node2=node2.next
        return None

# @lc code=end
