#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        pre = None
        node = head
        while node and node.next:
            while node and node.next and node.val == node.next.val:
                node = node.next

            if pre and pre.next != node:
                pre.next = node.next
            elif not pre and node != head:
                head = node.next
            else:
                pre = node

            node = node.next

        return head
# @lc code=end
