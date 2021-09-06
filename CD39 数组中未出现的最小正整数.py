"""
描述
给定一个无序数组arr，找到数组中未出现的最小正整数
例如arr = [-1, 2, 3, 4]。返回1
       arr = [1, 2, 3, 4]。返回5
[要求]
时间复杂度为O(n)O(n)，空间复杂度为O(1)O(1)

输入描述：
第一行为一个整数N。表示数组长度。
接下来一行N个整数表示数组内的数
输出描述：
输出一个整数表示答案
示例1
输入：
4
-1 2 3 4
复制
输出：
1
复制
示例2
输入：
4
1 2 3 4
复制
输出：
5
"""


class Solution:
    def GetMinNum(self, arr, n):
        l = 0
        r = n
        while(l < r):
            if arr[l] == l + 1:
                l += 1
            elif arr[l] <= l or arr[l] > r or arr[l] == arr[arr[l] - 1]:
                arr[l], arr[r - 1] = arr[r - 1], arr[l]
                r -= 1
            else:
                arr[l], arr[arr[l] - 1] = arr[arr[l] - 1], arr[l]
        return l + 1


if __name__ == '__main__':
    n = int(input())
    arr = [int(item) for item in input().split()]
    test = Solution()
    print(test.GetMinNum(arr, n))
