#
# @lc app=leetcode.cn id=2095 lang=python3
#
# [2095] 删除链表的中间节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        p = head
        while p:
            p = p.next
            length += 1
        index = length // 2
        pre = None
        p = head
        for _ in range(index):
            pre = p
            p = p.next
        if pre:
            pre.next = p.next
            return head
        else:
            return p.next

# @lc code=end
