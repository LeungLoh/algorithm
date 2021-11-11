"""
描述
实现反转单向链表和双向链表的函数。
如 1->2->3 反转后变成 3->2->1。
输入描述：
第一行一个整数 n，表示单链表的长度。

第二行 n 个整数 val 表示单链表的各个节点。

第三行一个整数 m，表示双链表的长度。

第四行 m 个整数 val 表示双链表的各个节点。
输出描述：
在给定的函数内返回相应链表的头指针。
示例1
输入：
3
1 2 3
4
1 2 3 4
输出：
3 2 1
4 3 2 1
"""


class LinkList:
    def __init__(self, v) -> None:
        self.value = v
        self.next = None


class LinkList2:
    def __init__(self, v) -> None:
        self.value = v
        self.next = None
        self.pre = None


class Solution:
    def ReverseLinkList(self, l):
        pre = None
        node = l
        next = None
        while node:
            next = node.next
            node.next = pre
            pre = node
            node = next
        return pre

    def ReverseLinkList2(self, l):
        pre = None
        node = l
        next = None
        while node:
            next = node.next
            node.next = pre
            node.pre = next
            pre = node
            node = next
        return pre


if __name__ == '__main__':
    n = input()
    vals1 = [int(item) for item in input().split()]
    m = input()
    vals2 = [int(item) for item in input().split()]

    l1 = LinkList(0)
    l2 = LinkList(0)
    p1 = l1
    p2 = l2
    for val in vals1:
        node = LinkList(val)
        p1.next = node
        p1 = node
    for val in vals2:
        node = LinkList(val)
        p2.next = node
        node.pre = p2
        p2 = node
    test = Solution()
    res = test.ReverseLinkList(l1.next)
    while res:
        print(res.value, end=" ")
        res = res.next
    print()
    res = test.ReverseLinkList(l2.next)
    while res:
        print(res.value, end=" ")
        res = res.next
