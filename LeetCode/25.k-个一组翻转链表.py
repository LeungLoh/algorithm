#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        pre=None
        next=None
        res=head
        end=head
        start=head
    
        while end:
            for _ in range(k-1):
                if not end:
                    break
                end=end.next
            if not end:
                break
            next=end.next
            end.next=None
            self.reverse(start)
            if not pre:
                res=end
            else:
                pre.next=end
            start.next=next
            pre=start
            start=next
            end=next                      
        return res
    
    def reverse(self,head):
        node=head
        pre=None
        next=None
        while node:
            next=node.next
            node.next=pre
            pre=node
            node=next
# @lc code=end
