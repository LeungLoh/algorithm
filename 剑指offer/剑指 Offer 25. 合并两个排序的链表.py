"""
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        node1 = l1
        node2 = l2
        node = res
        while node1 and node2:
            if node1.val < node2.val:
                p = node1
                node1 = node1.next
            else:
                p = node2
                node2 = node2.next
            p.next = None
            node.next = p
            node = node.next
        if node1:
            node.next = node1
        else:
            node.next = node2
        return res.next
