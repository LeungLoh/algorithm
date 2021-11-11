"""
描述
给定数组 arr 和整数 num，共返回有多少个子数组满足如下情况：
max(arr[i...j]) - min(arr[i...j]) <= num
max(arr[i...j])表示子数组arr[i...j]中的最大值，min[arr[i...j])表示子数组arr[i...j]中的最小值。

输入描述：
第一行输入两个数 n 和 num，其中 n 表示数组 arr 的长度
第二行输入n个整数Xi，表示数组arr中的每个元素
输出描述：
输出给定数组中满足条件的子数组个数
示例1
输入：
5 2 
1 2 3 4 5
输出：
12
"""


class Solution:
    def gersublist(self, n, arr, num):
        res = 0
        qmax = []
        qmin = []
        i = j = 0
        # 窗口size
        while i < n:
            while j < n:
                # 范围内的最大值/最小值
                if not qmax or qmax[-1] != j:
                    while qmax and arr[qmax[-1]] < arr[j]:
                        qmax.pop()
                    while qmin and arr[qmin[-1]] > arr[j]:
                        qmin.pop()
                    qmax.append(j)
                    qmin.append(j)
                if arr[qmax[0]] - arr[qmin[0]] > num:
                    break
                j += 1
            res += j - i
            # 窗口过期
            if qmax[0] == i:
                qmax.pop(0)
            if qmin[0] == i:
                qmin.pop(0)
            i += 1
        return res


if __name__ == '__main__':
    n, num = input().split()
    arr = [int(item)for item in input().split()]
    test = Solution()
    print(test.gersublist(int(n), arr, int(num)))
