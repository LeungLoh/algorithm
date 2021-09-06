"""
描述
给定一个无序单链表，实现单链表的选择排序(按升序排序)。
输入描述：
第一行一个整数 n，表示单链表的节点数量。
第二行 n 个整数 val 表示单链表的各个节点。
输出描述：
在给出的函数内返回给定链表的头指针。
示例1
输入：
5
1 3 2 4 5
输出：
1 2 3 4 5
"""


class LinkList:
    def __init__(self, v) -> None:
        self.value = v
        self.next = None


# class Solution:
#     def SelectSort(self, list):
#         node = list
#         res = LinkList(0)
#         resnode = res

#         while node:
#             p = node
#             pre = None
#             minnode = node
#             while p.next:
#                 if p.next.value < minnode.value:
#                     minnode = p.next
#                     pre = p
#                 p = p.next
#             if not pre:
#                 node = node.next
#             else:
#                 pre.next = minnode.next
#             minnode.next = None
#             resnode.next = minnode
#             resnode = resnode.next

#         return res.next


class Solution:
    def SelectSort(self, list):
        node = list

        while node:
            p = node.next
            minnode = node
            while p:
                if p.value < minnode.value:
                    minnode = p
                p = p.next
            if minnode != node:
                node.value, minnode.value = minnode.value, node.value
            node = node.next
        return list


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
    res = test.SelectSort(list.next)

    while res:
        print(res.value, end=" ")
        res = res.next
