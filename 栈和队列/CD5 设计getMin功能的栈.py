# -*- encoding: utf-8 -*-
'''
Author: leungloh
Email: liangquanle@360.cn
version: @v1.0
Date: 2021/08/23 15:19:51
'''


"""
描述
实现一个特殊功能的栈，在实现栈的基本功能的基础上，再实现返回栈中最小元素的操作。
输入描述：
第一行输入一个整数N，表示对栈进行的操作总数。

下面N行每行输入一个字符串S，表示操作的种类。

如果S为"push"，则后面还有一个整数X表示向栈里压入整数X。

如果S为"pop"，则表示弹出栈顶操作。

如果S为"getMin"，则表示询问当前栈中的最小元素是多少。
输出描述：
对于每个getMin操作，输出一行表示当前栈中的最小元素是多少。
示例1
输入：
6
push 3
push 2
push 1
getMin
pop
getMin
复制
输出：
1
2
复制
备注：
1<=N<=1000000

-1000000<=X<=1000000

数据保证没有不合法的操作
"""


class Solution:
    def __init__(self) -> None:
        self.s1 = list()
        self.s2 = list()

    def getMin(self):
        return self.s2[-1]

    def push(self, x):
        self.s1.append(x)
        if self.s2 == [] or self.s2[-1] > x:
            self.s2.append(x)
        else:
            self.s2.append(self.s2[-1])

    def pop(self):
        res = self.s1.pop()
        self.s2.pop()
        return res


if __name__ == "__main__":
    test = Solution()
    n = input()
    for i in range(int(n)):
        action = input().split(" ")
        if action[0] == "push":
            test.push(int(action[1]))
        elif action[0] == "pop":
            test.pop()
        elif action[0] == "getMin":
            print(test.getMin())
