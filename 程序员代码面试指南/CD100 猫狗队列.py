"""
描述
实现一种猫狗队列的结构，要求如下：
1. 用户可以调用 add 方法将 cat 或者 dog 放入队列中
2. 用户可以调用 pollAll 方法将队列中的 cat 和 dog 按照进队列的先后顺序依次弹出
3. 用户可以调用 pollDog 方法将队列中的 dog 按照进队列的先后顺序依次弹出
4. 用户可以调用 pollCat 方法将队列中的 cat 按照进队列的先后顺序依次弹出
5. 用户可以调用 isEmpty 方法检查队列中是否还有 dog 或 cat
6. 用户可以调用 isDogEmpty 方法检查队列中是否还有 dog
7. 用户可以调用 isCatEmpty 方法检查队列中是否还有 cat
输入描述：
第一行输入一个整数 n 表示 用户的操作总次数。

以下 n行 每行表示用户的一次操作

每行的第一个参数为一个字符串 s，若 s = “add”， 则后面接着有 “cat x”（表示猫）或者“dog x”（表示狗），其中的 x 表示猫狗的编号。
输出描述：
对于每个操作：

若为 “add”，则不需要输出。

以下仅列举几个代表操作，其它类似的操作输出同理。

若为 “pollAll”，则将队列中的 cat 和 dog 按照进队列的先后顺序依次弹出。(FIFO)，格式见样例。

若为 "isEmpty"，则检查队列中是否还有 dog 或 cat， 为空则输出 “yes”， 否则输出 “no”。
示例1
输入：
11
add cat 1
add dog 2
pollAll
isEmpty
add cat 5
isDogEmpty
pollCat
add dog 10
add cat 199
pollDog
pollAll
复制
输出：
cat 1
dog 2
yes
yes
cat 5
dog 10
cat 199
复制
备注：
1 \le n \le 10000001≤n≤1000000
保证每个猫和狗的编号x都不相同且 1 \le x \le 10000001≤x≤1000000
保证没有不合法的操作
"""


class Solution:
    def __init__(self) -> None:
        self.dog = list()
        self.cat = list()
        self.count = 0

    def add(self, s):
        animal = s.split(' ')[0]
        if animal == "cat":
            self.cat.append((s, self.count))
        elif animal == "dog":
            self.dog.append((s, self.count))
        self.count += 1

    def pollAll(self):
        while self.dog or self.cat:
            if not self.cat:
                self.pollDog()
            elif not self.dog:
                self.pollCat()
            else:
                if self.cat[0][1] < self.dog[0][1]:
                    print(self.cat.pop(0)[0])
                else:
                    print(self.dog.pop(0)[0])

    def pollCat(self):
        while(self.cat):
            print(self.cat.pop(0)[0])

    def pollDog(self):
        while(self.dog):
            print(self.dog.pop(0)[0])

    def isEmpty(self):
        if self.dog or self.cat:
            print("no")
        else:
            print("yes")

    def isCatEmpty(self):
        if self.cat:
            print("no")
        else:
            print("yes")

    def isDogEmpty(self):
        if self.dog:
            print("no")
        else:
            print("yes")


if __name__ == '__main__':
    test = Solution()
    n = int(input())
    for i in range(n):
        s = input()
        action = s.split(" ", 1)
        if action[0] == "add":
            test.add(action[1])
        elif action[0] == "pollAll":
            test.pollAll()
        elif action[0] == "pollDog":
            test.pollDog()
        elif action[0] == "pollCat":
            test.pollCat()
        elif action[0] == "isEmpty":
            test.isEmpty()
        elif action[0] == "isDogEmpty":
            test.isDogEmpty()
        elif action[0] == "isCatEmpty":
            test.isCatEmpty()
