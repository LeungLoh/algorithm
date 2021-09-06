"""
描述
给定一个单链表，实现一个调整单链表的函数，使得每 K 个节点之间的值逆序，如果最后不够 K 个节点一组，则不调整最后几个节点。
输入描述：
第一行一个整数 n，n 表示单链表的节点数量。

第二行 n 个整数 val 表示链表的各个节点的值。

第三行一个整数 K。
输出描述：
在给定的函数内返回链表的头指针。
示例1
输入：
5
1 2 3 4 5
3
输出：
3 2 1 4 5
"""


class LinkList:
    def __init__(self, v) -> None:
        self.value = v
        self.next = None


class Solution:
    def reverseKlist(self, list, k, n):
        res = None
        pre = None
        node = list
        start = list
        for i in range(1, n + 1):
            if i % k == 0:
                next = node.next
                node.next = None
                end = self.reverselist(start)
                if pre:
                    pre.next = end
                else:
                    res = end
                pre = start
                node = start
                start.next = next
                start = next

            node = node.next
        return res

    def reverselist(self, list):
        pre = None
        next = None
        node = list
        while node:
            next = node.next
            node.next = pre
            pre = node
            node = next
        return pre


if __name__ == '__main__':
    n = int(input())
    vals = [int(item) for item in input().split()]
    k = int(input())
    list = LinkList(0)
    p = list
    for val in vals:
        node = LinkList(val)
        p.next = node
        p = node
    test = Solution()
    res = test.reverseKlist(list.next, k, n)
    while res:
        print(res.value, end=" ")
        res = res.next
