"""
描述
用两个栈实现队列，支持队列的基本操作。
输入描述：
第一行输入一个整数N，表示对队列进行的操作总数。

下面N行每行输入一个字符串S，表示操作的种类。

如果S为"add"，则后面还有一个整数X表示向队列尾部加入整数X。

如果S为"poll"，则表示弹出队列头部操作。

如果S为"peek"，则表示询问当前队列中头部元素是多少。
输出描述：
对于每一个为"peek"的操作，输出一行表示当前队列中头部元素是多少。
示例1
输入：
6
add 1
add 2
add 3
peek
poll
peek
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

    def add(self, x):
        self.s1.append(x)

    def poll(self):
        if self.s2 == []:
            while self.s1 != []:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self):
        if self.s2 == []:
            while self.s1 != []:
                self.s2.append(self.s1.pop())
        return self.s2[-1]


if __name__ == '__main__':
    n = input()
    test = Solution()
    for i in range(int(n)):
        action = input().split(" ")
        if action[0] == "add":
            test.add(int(action[1]))
        elif action[0] == "peek":
            print(test.peek())
        elif action[0] == "poll":
            test.poll()
