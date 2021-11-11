"""
描述
给定一个整型数组arr，代表数值不同的纸牌排成一条线，玩家A和玩家B依次拿走每张纸牌，规定玩家A先拿，玩家B后拿，
但是每个玩家每次只能拿走最左和最右的纸牌，玩家A和玩家B绝顶聪明。请返回最后的获胜者的分数。
输入描述：
输出包括两行，第一行一个整数n(1≤n≤5000)，代表数组arr长度，第二行包含n个整数，第i个代表arr[i](1≤arr[i]≤10 5)。
输出描述：
输出一个整数，代表最后获胜者的分数。
示例1
输入：
4
1 2 100 4
输出：
101
"""


class Solution:

    def getMax(self, arr, n):
        return max(self.f(0, n - 1, arr), self.s(0, n - 1, arr))

    def f(self, i, j, arr):
        if i == j:
            return arr[i]
        return max(arr[i] + self.s(i + 1, j, arr), arr[j] + self.s(i, j - 1, arr))

    def s(self, i, j, arr):
        if i == j:
            return 0
        return min(self.f(i + 1, j, arr), self.f(i, j - 1, arr))


class Solution2:

    def getMax(self, arr, n):
        f = [[0] * n for _ in range(n)]
        s = [[0] * n for _ in range(n)]
        for j in range(n):
            f[j][j] = arr[j]
            for i in range(j - 1, -1, -1):
                f[i][j] = max(arr[i] + s[i + 1][j], arr[j] + s[i][j - 1])
                s[i][j] = min(f[i + 1][j], f[i][j - 1])
        return max(f[0][-1], s[0][-1])


class Solution3:
    smap = {}
    fmap = {}

    def getMax(self, arr, n):
        self.arr = arr
        return max(self.f(0, n - 1), self.s(0, n - 1))

    def f(self, i, j):

        if i == j:
            return self.arr[i]
        key = f'{i}_{j}'
        if key not in self.fmap:
            self.fmap[key] = max(self.arr[i] + self.s(i + 1, j), arr[j] + self.s(i, j - 1))
        return self.fmap[key]

    def s(self, i, j):
        if i == j:
            return 0
        key = f'{i}_{j}'
        if key not in self.smap:
            self.smap[key] = min(self.f(i + 1, j), self.f(i, j - 1))
        return self.smap[key]


if __name__ == '__main__':
    n = int(input())
    arr = [int(item) for item in input().split()]
    test = Solution2()
    print(test.getMax(arr, n))
