#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        return self.merge(0, len(lists) - 1, lists)

    def merge(self, left, right, lists):
        if left > right:
            return
        if left == right:
            return lists[left]
        mid = left + (right - left) // 2
        l1 = self.merge(left, mid, lists)
        l2 = self.merge(mid + 1, right, lists)
        return self.mergelist(l1, l2)

    def mergelist(self, head1, head2):
        node1, node2 = head1, head2
        res = ListNode(0)
        p = res
        while node1 and node2:
            if node1.val < node2.val:
                node = ListNode(node1.val)
                node1 = node1.next
            else:
                node = ListNode(node2.val)
                node2 = node2.next
            p.next = node
            p = p.next
        if node1:
            p.next = node1
        if node2:
            p.next = node2
        return res.next
# @lc code=end
