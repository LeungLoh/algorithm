"""
描述
给定一个无序数组arr，其中元素可正、可负、可0。求arr所有子数组中正数与负数个数相等的最长子数组的长度。
[要求]
时间复杂度为O(n)O(n)，空间复杂度为O(n)O(n)
输入描述：
第一行一个整数N，表示数组长度
接下来一行有N个数表示数组中的数
输出描述：
输出一个整数表示答案
示例1
输入：
5
1 -2 1 1 1
复制
输出：
2
"""


class Solution:
    def GetMaxSubList(self, n, arr):
        m = {0: -1}
        a = ans = 0
        for i in range(n):
            if arr[i] > 0:
                a += 1
            elif arr[i] < 0:
                a -= 1
            if a not in m.keys():
                m[a] = i
            else:
                ans = max(ans, i - m[a])
        return ans


if __name__ == '__main__':
    n = int(input())
    arr = [int(item) for item in input().split()]
    test = Solution()
    print(test.GetMaxSubList(n, arr))
