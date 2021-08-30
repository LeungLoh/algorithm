"""
描述
假设链表中每一个节点的值都在 0 - 9 之间，那么链表整体就可以代表一个整数。
给定两个这种链表，请生成代表两个整数相加值的结果链表。
例如：链表 1 为 9->3->7，链表 2 为 6->3，最后生成新的结果链表为 1->0->0->0。
输入描述：
第一行两个整数 n 和 m，分别表示两个链表的长度。

第二行 n 个整数 ai 表示第一个链表的节点。

第三行 m 个整数 bi 表示第二个链表的节点。
输出描述：
输出一行整数表示结果链表。
示例1
输入：
3 2
9 3 7
6 3
输出：
1 0 0 0
"""


class LinkList:
    def __init__(self, v) -> None:
        self.value = v
        self.next = None


class Solution:
    def addlist(self, list1, list2):
        s1 = list()
        s2 = list()
        node1 = list1
        node2 = list2
        while node1:
            s1.append(node1.value)
            node1 = node1.next
        while node2:
            s2.append(node2.value)
            node2 = node2.next
        flag = False
        res = LinkList(0)
        node = res
        while s1 or s2:
            if not s1:
                value = s2.pop()
            elif not s2:
                value = s1.pop()
            else:
                value = s1.pop() + s2.pop()
            value = value if not flag else value + 1
            node.next = LinkList(value % 10)
            node = node.next
            flag = True if value >= 10 else False

        if flag:
            node.next = LinkList(1)
        return self.reversekist(res.next)

    def reversekist(self, list):
        node = list
        pre = None
        next = None
        while node:
            next = node.next
            node.next = pre
            pre = node
            node = next
        return pre


if __name__ == '__main__':
    n, m = input().split()
    vals1 = [int(item) for item in input().split()]
    vals2 = [int(item) for item in input().split()]
    list1 = LinkList(0)
    list2 = LinkList(0)
    p = list1
    for val in vals1:
        node = LinkList(val)
        p.next = node
        p = node
    p = list2
    for val in vals2:
        node = LinkList(val)
        p.next = node
        p = node
    test = Solution()
    res = test.addlist(list1.next, list2.next)

    while res:
        print(res.value, end=" ")
        res = res.next
