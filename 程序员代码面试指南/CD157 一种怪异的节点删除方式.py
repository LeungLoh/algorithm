"""
描述
链表节点值类型为 int 类型，给定一个链表中的节点 node，但不给定整个链表的头节点。如何在链表中删除 node ? 请实现这个函数。
输入描述：
给出一个单链表的节点。
输出描述：
不需要返回值。
示例1
输入：
5 
1 2 3 4 5
3
输出：
1 2 4 5
"""


class LinkList:
    def __init__(self, v) -> None:
        self.value = v
        self.next = None


class Solution:
    def Deletenode(self, node):
        p = node
        pre = None
        while p.next:
            p.value = p.next.value
            pre = p
            p = p.next
        pre.next = None


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
    node = list.next
    for _ in range(k - 1):
        node = node.next
    test = Solution()
    test.Deletenode(node)

    while list.next:
        print(list.next.value, end=" ")
        list = list.next
