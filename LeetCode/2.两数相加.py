#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        node = res
        flag = False
        node1 = l1
        node2 = l2
        while node1 or node2:
            if not node1:
                val = node2.val + 1 if flag else node2.val
                flag = True if val >= 10 else False
                node.next = ListNode(val % 10)
                node2 = node2.next
            elif not node2:
                val = node1.val + 1 if flag else node1.val
                flag = True if val >= 10 else False
                node.next = ListNode(val % 10)
                node1 = node1.next
            else:


                val = node1.val + node2.val
                val = val + 1 if flag else val
                flag = True if val >= 10 else False
                node.next = ListNode(val % 10)
                node1 = node1.next
                node2 = node2.next
            node=node.next

        if flag:
            node.next = ListNode(1)
        return res.next


# @lc code=end
