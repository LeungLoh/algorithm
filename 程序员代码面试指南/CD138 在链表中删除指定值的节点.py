"""
描述
给出一个链表和一个整数 num，输出删除链表中节点值等于 num 的节点之后的链表。
输入描述：
第一行一个整数 n，n 表示单链表的节点数量。

第二行 n 个整数表示单链表的各个节点的值。

第三行一个整数 num。
输出描述：
在给定的函数中返回指定链表的头指针。
示例1
输入：
4 
1 2 3 4
3
输出：
1 2 4
"""


class LinkList:
    def __init__(self, v) -> None:
        self.value = v
        self.next = None


class Solution:
    def DeleteNode(self, list, num):

        while list.value == num:
            list = list.next
        node = list
        while node.next:
            if node.next.value == num:
                node.next = node.next.next
            else:
                node = node.next
        return list


if __name__ == '__main__':
    n = int(input())
    vals = [int(item) for item in input().split()]
    num = int(input())
    list = LinkList(0)
    p = list
    for val in vals:
        node = LinkList(val)
        p.next = node
        p = node
    test = Solution()
    res = test.DeleteNode(list.next, num)
    while res:
        print(res.value, end=" ")
        res = res.next
