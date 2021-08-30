"""
描述
给定一个单链表，在链表中把第 L 个节点到第 R 个节点这一部分进行反转。
输入描述：
n 表示单链表的长度。

val 表示单链表各个节点的值。

L 表示翻转区间的左端点。

R 表示翻转区间的右端点。
输出描述：
在给定的函数中返回指定链表的头指针。
示例1
输入：
5
1 2 3 4 5
1 3
输出：
3 2 1 4 5
"""


class LinkList:
    def __init__(self, v) -> None:
        self.value = v
        self.next = None


class Solution:
    def ReverseSubList(self, list, L, R):
        left = None
        right = None
        sublist = None
        pre = None
        p = list
        for _ in range(L - 1):
            pre = p
            p = p.next
        left = pre
        sublist = p
        for _ in range(R - L):
            p = p.next
        right = p.next
        p.next = None
        head, end = self.ReverseList(sublist)
        end.next = right
        if not left:
            return head
        else:
            left.next = head
            return list

    def ReverseList(self, list):
        pre = None
        next = None
        node = list
        while node:
            next = node.next
            node.next = pre
            pre = node
            node = next
        return pre, list


if __name__ == '__main__':
    n = input()
    vals = [int(item) for item in input().split()]
    L, R = input().split()
    list = LinkList(0)
    p = list
    for val in vals:
        node = LinkList(val)
        p.next = node
        p = node
    test = Solution()
    res = test.ReverseSubList(list.next, int(L), int(R))
    while res:
        print(res.value, end=" ")
        res = res.next
