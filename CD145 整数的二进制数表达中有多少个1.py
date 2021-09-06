"""
描述
给定一个32位整数n，返回该整数二进制形式1的个数。
输入描述：
输入一个整数，代表n，n为32为整数。
输出描述：
输出一个整数，代表n的二进制表达式中1的个数。
示例1
输入：
1
复制
输出：
1
复制
示例2
输入：
-2
复制
输出：
31
"""


class Solution:
    def GetOneNum(self, num):
        res = 0
        if num < 0:
            num += pow(2, 32)

        while num:
            res += num & 1
            num >>= 1
        return res


if __name__ == '__main__':
    num = int(input())
    test = Solution()
    print(test.GetOneNum(num))
