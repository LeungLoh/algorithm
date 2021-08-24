# -*- encoding: utf-8 -*-
'''
Author: leungloh
Email: liangquanle@360.cn
version: @v1.0
Date: 2021/08/24 10:16:37
'''

"""
描述
一个栈中元素的类型为整型，现在想将该栈从顶到底按从大到小的顺序排序，只许申请一个栈。除此之外，可以申请新的变量，但不能申请额外的数据结构。如何完成排序？
输入描述：
第一行输入一个N，表示栈中元素的个数
第二行输入N个整数a_ia 
i
​
 表示栈顶到栈底的各个元素
输出描述：
输出一行表示排序后的栈中栈顶到栈底的各个元素。
示例1
输入：
5
5 8 4 3 6
输出：
8 6 5 4 3
"""


class Solution:
    def sortstack(self, s):
        res = list()
        while s:
            value = s.pop()
            count = 0
            while res and value < res[-1]:
                s.append(res.pop())
                count += 1
            res.append(value)
            for _ in range(count):
                res.append(s.pop())
        return res


if __name__ == '__main__':
    n = input()
    s = [int(item) for item in input().split(' ')]
    test = Solution()
    res = [str(item)for item in test.sortstack(s)]
    print(" ".join(res[::-1]))
