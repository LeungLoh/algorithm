#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p1 = head
        p2 = head
        pre = None
        for _ in range(n):
            p1 = p1.next
        while p1:
            pre = p2
            p1 = p1.next
            p2 = p2.next
        if not pre:
            return head.next
        else:
            pre.next = pre.next.next
        return head
# @lc code=end
