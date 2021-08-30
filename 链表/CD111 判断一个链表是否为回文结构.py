"""
描述
给定一个链表，请判断该链表是否为回文结构。
输入描述：
n 表示链表的长度
ai 表示链表的各个节点的值。
输出描述：
如果为回文结构输出 "true" , 否则输出 "false"。
示例1
输入：
4
1 2 2 1
输出：
true
"""


class LinkList:
    def __init__(self, v) -> None:
        self.value = v
        self.next = None


class Solution:
    def checklist(self, list, n):
        res = True
        mid = list
        for _ in range(int(n / 2)):
            mid = mid.next

        def reverselist(list):
            node = list
            next = None
            pre = None
            while node:
                next = node.next
                node.next = pre
                pre = node
                node = next
            return pre

        end = reverselist(mid)
        right = end
        left = list
        while right:
            if right.value != left.value:
                res = False
                break
            right = right.next
            left = left.next

        reverselist(end)
        if res:
            print("true")
        else:
            print("false")
        # return res


if __name__ == '__main__':
    n = input()
    vals = [int(item) for item in input().split()]
    list = LinkList(0)
    p = list
    for val in vals:
        node = LinkList(val)
        p.next = node
        p = node
    test = Solution()
    test.checklist(list.next, int(n))
