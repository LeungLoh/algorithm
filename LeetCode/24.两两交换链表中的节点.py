#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        pre = None
        node1 = head
        node2 = head.next
        res = node2
        while node1 and node2:
            if pre:
                pre.next = node2
            node1.next = node2.next
            node2.next = node1

            pre = node1
            if node1.next and node1.next.next:
                node1 = node1.next
                node2 = node1.next
            else:
                break
        return res


# @lc code=end
