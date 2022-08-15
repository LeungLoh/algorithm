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
        if len(lists)==1:
            return lists[0]
        return self.mergelist(lists)
        
    def mergelist(self,lists):
        head=lists[0]
        for i in range(1,len(lists)):
            head=self.merge(head,lists[i])
        return head

    def merge(self,head1,head2):
        head=ListNode(0)
        node=head
        p1=head1
        p2=head2
        while p1 and p2:
            if p1.val>p2.val:
                node.next=p2
                p2=p2.next
                node=node.next
            else:
                node.next=p1
                p1=p1.next
                node=node.next
        if p1:
            node.next=p1
        if p2:
            node.next=p2
        return head.next
# @lc code=end
