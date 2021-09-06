"""
描述
一个不含有负数的数组可以代表一圈环形山，每个位置的值代表山的高度。比如，{3,1,2,4,5}，{4,5,3,1,2}或{1,2,4,5,3}都代表同样结构的环形山。3->1->2->4->5->3 方向叫作 next 方向(逆时针)，3->5->4->2->1->3 方向叫作 last 方向(顺时针)。
山峰 A 和 山峰 B 能够相互看见的条件为:
1. 如果 A 和 B 是同一座山，认为不能相互看见。
2. 如果 A 和 B 是不同的山，并且在环中相邻，认为可以相互看见。
3. 如果 A 和 B 是不同的山，并且在环中不相邻，假设两座山高度的最小值为 min。如果 A 通过 next 方向到 B 的途中没有高度比 min 大的山峰，或者 A 通过 last 方向到 B 的途中没有高度比 min 大的山峰，认为 A 和 B 可以相互看见。
问题如下：
给定一个含有负数可能有重复值的数组 arr，请问有多少对山峰能够相互看见？ 
输入描述：
第一行给出一个整数 n，表示山峰的数量。

以下一行 n 个整数表示各个山峰的高度。
输出描述：
输出一行表示答案。
示例1
输入：
5
3 1 2 4 5
输出：
7
"""


class LinkList:
    def __init__(self, v) -> None:
        self.value = v
        self.next = None


class Solution:
    def getviewhill(self, list):
        pass

    def getsingelview(self, start):
        s = []
        node = start.next
        while node.next != node and node.value <= start.value:
            if s and s[-1].value >=


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
