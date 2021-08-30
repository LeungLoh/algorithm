"""
描述
给定一个链表，再给定一个整数 pivot，请将链表调整为左部分都是值小于 pivot 的节点，中间部分都是值等于 pivot 的节点， 右边部分都是大于 pivot 的节点。
除此之外，对调整后的节点顺序没有更多要求。
输入描述：
第一行两个整数 n 和 pivot，n 表示链表的长度。

第二行 n 个整数 ai 表示链表的节点。
输出描述：
请在给定的函数内返回链表的头指针。
示例1
输入：
5 3
9 0 4 5 1
复制
输出：
1 0 4 5 9
"""


class LinkList:
    def __init__(self, v) -> None:
        self.value = v
        self.next = None


class Solution:
    def parition(self, list, pivot):
        gt = LinkList(0)
        eq = LinkList(0)
        lt = LinkList(0)
        gt_node = gt
        eq_node = eq
        lt_node = lt
        node = list
        while node:
            next = node.next
            node.next = None
            if node.value < pivot:
                gt_node.next = node
                gt_node = node
            elif node.value == pivot:
                eq_node.next = node
                eq_node = node
            else:
                lt_node.next = node
                lt_node = node
            node = next

        if lt.next:
            eq_node.next = lt.next
        if eq.next:
            gt_node.next = eq.next
        return gt.next


if __name__ == '__main__':
    n, pivot = input().split()
    vals = [int(item) for item in input().split()]
    list = LinkList(0)
    p = list
    for val in vals:
        node = LinkList(val)
        p.next = node
        p = node
    test = Solution()
    res = test.parition(list.next, int(pivot))
    while res:
        print(res.value, end=" ")
        res = res.next
