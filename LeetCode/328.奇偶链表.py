#
# @lc app=leetcode.cn id=328 lang=python3
#
# [328] 奇偶链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    def oddEvenList(self, head):
        if not head:
            return head
        length = 0
        node = head
        while node:
            node = node.next
            length += 1
        pre = head
        right = ListNode()
        cur = head
        node = right
        for i in range(1, length + 1):
            _next = cur.next
            if i % 2 == 0:
                node.next = cur
                pre.next = cur.next
                node = cur
                cur.next = None
            else:
                pre = cur
            cur = _next

        pre.next = right.next

        return head

# @lc code=end
