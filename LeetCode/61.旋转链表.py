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
        end = head
        while node:
            length += 1
            end = node
            node = node.next
        k = k % length
        if not k:
            return head
        p1, p2 = head, head
        for _ in range(k):
            p1 = p1.next
        while p1 and p1.next:
            p1 = p1.next
            p2 = p2.next
        _next = p2.next
        p2.next = None
        end.next = head
        return _next


# @lc code=end
