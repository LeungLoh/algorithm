#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        k = k % length
        if k == 0:
            return head

        p1 = head
        p2 = head
        for _ in range(k + 1):
            p1 = p1.next
        while p1:
            p1 = p1.next
            p2 = p2.next
        res = p2.next
        end = p2.next
        p2.next = None

        while end.next:
            end = end.next
        end.next = head
        return res

# @lc code=end
