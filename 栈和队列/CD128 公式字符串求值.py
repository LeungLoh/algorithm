# -*- encoding: utf-8 -*-
'''
Author: leungloh
Email: liangquanle@360.cn
version: @v1.0
Date: 2021/08/24 16:38:58
'''

"""
描述
给定一个字符串str，str表示一个公式，公式里可以有整数，加减乘除和左右括号，返回公式的计算结果（注意：题目中所有运算都是整型运算，向下取整,且保证数据合法，不会出现除0等情况）。
输入描述：
输出一行字符串，代表（保证str计算的结果不会出现除零，int溢出等情况）。
输出描述：
输出一个整数，代表表达式的计算结果。
示例1
输入：
48*((70-65)-43)+8*1
输出：
-1816
示例2
输入：
3+1*4
输出：
"""


class Solution:
    def calculate(self, n, arr):
        s = list()
        i = 0
        while i < n:
            value1 = ""
            value2 = ""
            while i < n and arr[i].isdigit():
                value1 += arr[i]
                i += 1
            if i == n - 1:
                break

            operator = arr[i]
            i += 1
            if arr[i] == "(":
                value2, index = self.calculate(n - i - 1, arr[i + 1:])
                i += index + 1
            else:
                while i < n and arr[i].isdigit():
                    value2 += arr[i]
                    i += 1

            if operator == '+':
                s.append(int(value1) + int(value2))
            elif operator == "-":
                s.append(int(value1) + int(value2))
            elif operator == "*":
                s.append(int(value1) * int(value2))
            elif operator == "/":
                s.append(int(value1) / int(value2))
            elif operator == "(":
                break
        return sum(s), i


if __name__ == '__main__':
    s = input()
    test = Solution()
    print(test.calculate(len(s), s))
