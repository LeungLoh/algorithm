"""
描述
给定一个链表，实现删除链表第 K 个节点的函数。
输入描述：
n 表示链表的长度。

m 表示删除链表第几个节点。

val 表示链表节点的值。
输出描述：
在给定的函数中返回链表的头指针。
示例1
输入：
5 3
1 2 3 4 5
输出：
1 2 4 5
"""


class LinkList:
    def __init__(self, v) -> None:
        self.value = v
        self.next = None


class Solution:
    def deleteknode(self, k, l):
        p = l
        for _ in range(k - 2):
            p = p.next
        p.next = p.next.next
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
