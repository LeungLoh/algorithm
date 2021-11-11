"""
输入两个链表，找出它们的第一个公共节点。

如下面的两个链表：



在节点 c1 开始相交。

 

示例 1：



输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Reference of the node with value = 8
输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
 

示例 2：



输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Reference of the node with value = 2
输入解释：相交节点的值为 2 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
 

示例 3：



输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：null
输入解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
解释：这两个链表不相交，因此返回 null。

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        ring1, ringA = self.checkring(headA)
        ring2, ringB = self.checkring(headB)
        if (ring1 and not ring2) or (not ring1 and ring2):
            return None
        if not ring1 and not ring2:
            return self.checknotring(headA, headB)
        else:
            return self.checekring(headA, headB, ringA, ringB)

    def checkring(self, head):
        if not head.next:
            return False, None
        p1 = head.next
        p2 = head.next.next
        while p1 and p2 and p2.next:
            if p1 == p2:
                return True, p1
            p1 = p1.next
            p2 = p2.next.next
        return False, None

    def checknotring(self, headA, headB, endflag=None):
        length1, length2 = 0, 0
        node1, node2 = headA, headB
        while node1 != endflag:
            node1 = node1.next
            length1 += 1
        while node2 != endflag:
            node2 = node2.next
            length2 += 1
        node1, node2 = headA, headB
        if length1 > length2:
            for _ in range(length1 - length2):
                node1 = node1.next
        elif length1 < length2:
            for _ in range(length2 - length1):
                node2 = node2.next
        while node1 != endflag:
            if node1 == node2:
                return node1
            node1 = node1.next
            node2 = node2.next
        return None

    def checekring(self, headA, headB, ringA, ringB):
        if ringA == ringB:
            return self.checknotring(headA, headB, ringA)
        else:
            node1 = ringA.next
            while node1 != ringA:
                if node1 == ringB:
                    return node1
                node1 = node1.next
            return None
