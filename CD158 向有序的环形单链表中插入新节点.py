"""
描述
一个环形单链表从头节点 head 开始不降序，同时由最后的节点指回头节点。给定这样一个环形单链表的头节点 head 和 一个整数 num， 请生成节点值为 num 的新节点，并插入到这个环形链表中，保证调整后的链表依然有序。
输入描述：
环形单链表的头节点 head 和 一个整数 num。
输出描述：
在给定的函数内返回新的环形单链表的头指针。
示例1
输入：
5
1 2 3 4 5
6
复制
输出：
1 2 3 4 5 6
"""


class LinkList:
    def __init__(self, v) -> None:
        self.value = v
        self.next = None


class Solution:
    def InsertNode(self, list, value):
        pre = list
        node = list.next
        while node != list:
            if pre.value <= value and node.value >= value:
                insertnode = LinkList(value)
                insertnode.next = node
                pre.next = insertnode
                break
            pre = node
            node = node.next

        if node == list:
            insertnode = LinkList(value)
            insertnode.next = node
            pre.next = insertnode


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
    p.next = list.next
    test = Solution()
    test.InsertNode(list.next, k)
    for _ in range(n + 1):
        print(list.next.value, end=" ")
        list = list.next
