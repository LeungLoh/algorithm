"""
描述
据说著名犹太历史学家 Josephus 有过以下故事：在罗马人占领乔塔帕特后，39 个犹太人与 Josephus 及他的朋友躲到一个洞中，39 个犹太人决定宁愿死也不要被敌人抓到，于是决定了一种自杀方式，41 个人排成一个圆圈，由第 1 个人开始报数，报数到 3 的人就自杀，然后再由下一个人重新报 1，报数到 3 的人再自杀，这样依次下去，直到剩下最后一个人时，那个人可以自由选择自己的命运。这就是著名的约瑟夫问题。现在请用单向环形链表得出最终存活的人的编号。
输入描述：
一行两个整数 n，m，n 表示链表的长度，m 表示每报数到 m 就自杀。
输出描述：
输出最后存活的人的编号(编号从 1 开始到 n)。
示例1
输入：
5 2
输出：
3
"""


if __name__ == '__main__':
    n, m = map(int, input().split())
    l = list(range(1, n + 1))
    res = 0
    for i in range(1, n + 1):
        res = (res + m) % i
    print(res + 1)
