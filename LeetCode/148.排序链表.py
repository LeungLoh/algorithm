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
            node = node.next
            length += 1
        return self.sort(head, length)

    def sort(self, head, length):
        if length == 1:
            return head
        if length == 2:
            if head.val > head.next.val:
                node = head.next
                node.next = head
                head.next = None
                return node
            else:
                return head
        mid = length // 2
        node1 = head
        node2 = head
        pre = None
        for _ in range(mid):
            pre = node2
            node2 = node2.next
        pre.next = None
        nnode1 = self.sort(node1, mid)
        nnode2 = self.sort(node2, length - mid)
        return self.merge(nnode1, nnode2)

    def merge(self, head1, head2):
        node1 = head1
        node2 = head2
        nhead = ListNode(0)
        node = nhead
        while node1 and node2:
            if node1.val < node2.val:
                node.next = node1
                node1 = node1.next
            else:
                node.next = node2
                node2 = node2.next
            node = node.next
            node.next = None
        if node1:
            node.next = node1
        if node2:
            node.next = node2
        return nhead.next


# @lc code=end
