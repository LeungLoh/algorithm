"""
描述
给定一个单链表的头部节点 head，链表长度为 N，如果 N 是偶数，那么前 N / 2 个节点算作左半区，后 N / 2 个节点算作右半区；如果 N 为奇数，那么前 N / 2 个节点算作左半区，后 N / 2 + 1个节点算作右半区。左半区从左到右依次记为 L1->L2->...，右半区从左到右依次记为 R1->R2->...，请将单链表调整成 L1->R1->L2->R2->... 的形式。
输入描述：
单链表的头节点 head。
输出描述：
在给定的函数内返回链表的头指针。
示例1
输入：
6
1 2 3 4 5 6
复制
输出：
1 4 2 5 3 6

"""


class LinkList:
    def __init__(self, v) -> None:
        self.value = v
        self.next = None


class Solution:
    def LRlist(self, list, n):
        left = list
        right = None
        res = LinkList(0)
        flag = True
        node = list
        for _ in range(int(n / 2) - 1):
            node = node.next
        right = node.next
        node.next = None
        node = res
        while left:
            if flag:
                node.next = left
                left = left.next
            else:
                node.next = right
                right = right.next
            node = node.next
            flag = not flag
        if right:
            node.next = right
        return res.next


if __name__ == '__main__':
    n = int(input())
    vals = [int(item) for item in input().split()]
    list = LinkList(0)
    p = list
    for val in vals:
        node = LinkList(val)
        p.next = node
        p = node
    test = Solution()
    res = test.LRlist(list.next, n)
    while res:
        print(res.value, end=" ")
        res = res.next
