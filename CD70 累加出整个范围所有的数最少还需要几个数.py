"""
描述
给定一个正数数组arr 和一个正数range，可以选择arr 中的任意个数字加起来的和为sum。
返回最小需要往arr 中添加几个数，使得sum 可以取到1∼range范围上的每一个数。
给出的数组不保证有序！
输入描述：
第一行一个整数N, K。表示数组长度以及range
接下来一行N个整数表示数组内的元素
输出描述：
输出一个整数表示答案
示例1
输入：
4 15
1 2 3 7
输出：
1
说明：
想累加得到1∼15范围上的所有的数，arr还缺14这个数，所以返回1
示例2
输入：
3 14
1 5 7
输出：
2
复制
说明：
想累加得到1~14范围上所有的数，arr还缺2和4，所以返回2。
"""


class Solution:
    def GetMinAddNum(self, arr, n, num):
        arr.sort()
        res = 0
        cur = 0
        while cur < num:
            if arr:
                top = arr[0]
                if top <= cur + 1:
                    cur += top
                    arr = arr[1:]
                else:
                    res += 1
                    cur += cur + 1
            else:
                res += 1
                cur += cur + 1
        return res


if __name__ == '__main__':
    n, num = input().split()
    arr = [int(item) for item in input().split()]
    test = Solution()
    print(test.GetMinAddNum(arr, int(n), int(num)))
