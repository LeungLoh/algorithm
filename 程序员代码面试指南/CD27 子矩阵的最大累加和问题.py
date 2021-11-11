"""
描述
给定一个矩阵matrix，其中的值有正、有负、有0，返回子矩阵的最大累加和
例如，矩阵matrix为：
-90 48 78
64 -40 64
-81 - 7 66
其中，最大的累加和的子矩阵为：
48 78
-40 64
-7 66
所以返回累加和209。
例如，matrix为：
-1 -1 -1
-1 2 2
-1 -1 -1
其中，最大累加和的子矩阵为：
2 2
所以返回4

输入描述：
第一行有两个整数N，M。分别表示矩阵的行数/列数
接下来N行，每行M个整数表示矩阵内的数
输出描述：
输出一个整数表示答案
示例1
输入：
3 3
-90 48 78
64 -40 64
-81 -7 66 
输出：
209 
示例2
输入：
3 3
-1 -1 -1
-1 2 2
-1 -1 -1 
输出：
4
"""


class Solution:
    def GetMaxSum(self, matrix, n, m):
        res = 0
        for i in range(n):
            help = [0] * m
            for j in range(i, n):
                cur = 0
                for k in range(m):
                    help[k] += matrix[j][k]
                    cur += help[k]
                    res = max(res, cur)
                    cur = 0 if cur < 0 else cur
        return res


if __name__ == '__main__':
    n, m = input().split()
    arr = []
    for i in range(int(n)):
        arr.append([int(item) for item in input().split()])
    test = Solution()
    print(test.GetMaxSum(arr, int(n), int(m)))
