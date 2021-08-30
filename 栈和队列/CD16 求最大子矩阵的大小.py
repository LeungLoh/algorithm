"""
描述
给定一个整型矩阵 map，其中的值只有 0 和 1 两种，求其中全是 1 的所有矩形区域中，最大的矩形区域里 1 的数量。
输入描述：
第一行输入两个整数 n 和 m，代表 n*m 的矩阵
接下来输入一个 n*m 的矩阵
输出描述：
输出其中全是 1 的所有矩形区域中，最大的矩形区域里 1 的数量。
示例1
输入：
1 4
1 1 1 0
输出：
3
说明：
最大的矩形区域有3个1，所以返回3
"""


class Solution:
    def getMaxSum(self, n, m, arr):
        height = [0] * m
        res = 0
        for i in range(n):
            for j in range(m):
                height[j] = 0 if arr[i][j] == 0 else height[j] + 1

            res = max(res, self.getMaxSumFromButtom(height, m))
        return res

    def getMaxSumFromButtom(self, height, length):
        s = []
        res = 0
        for index in range(length):
            while s and height[s[-1]] >= height[index]:
                top = s.pop()
                l = -1 if not s else s[-1]
                res = max(res, height[top] * (index - l - 1))

            s.append(index)
        while(s):
            top = s.pop()
            l = -1 if not s else s[-1]
            res = max(res, height[top] * (length - l - 1))
        return res


if __name__ == '__main__':
    n, m = input().split()
    arr = [[int(item) for item in input().split()]for i in range(int(n))]
    test = Solution()
    print(test.getMaxSum(int(n), int(m), arr))
