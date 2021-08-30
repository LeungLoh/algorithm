"""
描述
给定一个整形数组arr，已知其中所有的值都是非负的，将这个数组看作一个容器，请返回容器能装多少水。
具体请参考样例解释
输入描述：
第一行一个整数N，表示数组长度。

接下来一行N个数表示数组内的数。
输出描述：
输出一个整数表示能装多少水。
示例1
输入：
6
3 1 2 5 2 4
输出：
5
示例2
输入：
5
4 5 1 3 2
输出：
2
"""


class Solution:
    def getMaxCol(self, arr, n):
        col = 0
        leftH, rightH = 0, 0
        maxH = max(arr)
        maxindex = arr.index(maxH)

        for i in range(maxindex):
            if arr[i] < leftH:
                col += leftH - arr[i]
            else:
                leftH = arr[i]
        for i in range(n - 1, maxindex, -1):
            if arr[i] < rightH:
                col += rightH - arr[i]
            else:
                rightH = arr[i]
        return col


if __name__ == '__main__':
    n = int(input())
    arr = [int(item) for item in input().split()]
    test = Solution()
    print(test.getMaxCol(arr, n))
