"""
描述
给出一个单链表，返回删除单链表的倒数第 K 个节点的链表。
输入描述：
n 表示链表的长度。
val 表示链表中节点的值。
输出描述：
在给定的函数内返回链表的头指针。
示例1
输入：
5 4
1 2 3 4 5
输出：
1 3 4 5
"""


class LinkList:
    def __init__(self, v) -> None:
        self.value = v
        self.next = None


class Solution:
    def deletereknode(self, k, l):
        p1 = l
        p2 = l
        for _ in range(k):
            p1 = p1.next
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        p2.next=p2.next.next
        return l


if __name__ == '__main__':
    n, k = input().split()
    vals = [int(item) for item in input().split()]
    l = LinkList(0)
    p = l
    for val in vals:
        node = LinkList(val)
        p.next = node
        p = node
    test = Solution()
    res = test.deletereknode(int(k), l.next)
    while res:
        print(res.value, end=" ")
        res = res.next
