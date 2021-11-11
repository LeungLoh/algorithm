"""
描述
给定两个升序的单链表的头节点 head1 和 head2，请合并两个升序链表， 合并后的链表依然升序，并返回合并后链表的头节点。
输入描述：
两个升序的单链表的头节点 head1 和 head2
输出描述：
在给定的函数内返回新链表的头指针。
示例1
输入：
5
1 2 3 4 5
6
7 8 9 10 11 12
输出：
1 2 3 4 5 7 8 9 10 11 12

"""


class LinkList:
    def __init__(self, v) -> None:
        self.value = v
        self.next = None


class Solution:
    def mergelist(self, list1, list2):
        node1 = list1
        node2 = list2
        res = LinkList(0)
        node = res
        while node1 and node2:
            if node1.value < node2.value:
                node.next = node1
                node1 = node1.next
            else:
                node.next = node2
                node2 = node2.next
            node = node.next
        node.next = node1 if node1 else node2
        return res.next


if __name__ == '__main__':
    n = int(input())
    vals1 = [int(item) for item in input().split()]
    m = int(input())
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
    res = test.mergelist(list1.next, list2.next)
    while res:
        print(res.value, end=" ")
        res = res.next
