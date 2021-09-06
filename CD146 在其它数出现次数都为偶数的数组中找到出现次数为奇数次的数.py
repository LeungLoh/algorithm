"""
描述
给一个数组arr，其中只有一个数出现了奇数次，其它数出现了偶数次，打印这个数。
输入描述：
输出包含两行，第一行包含一个整数n，代表数组arr长度，第二行有n个数，代表数组arrarr_i 为32位整数arr 
i
​
 为32位整数。
输出描述：
输出一个整数，代表出现次数为奇数次的那个数。
示例1
输入：
5
3 1 3 1 2
输出：
2
示例2
输入：
3
6 6 3
输出：
3
"""


class Solution:
    def GetSingleNum(self, arr, n):
        sum = 0
        for v in arr:
            sum ^= v
        return sum


if __name__ == '__main__':
    n = int(input())
    arr = [int(item) for item in input().split()]
    test = Solution()
    res = test.GetSingleNum(arr, n)
    print(res)
