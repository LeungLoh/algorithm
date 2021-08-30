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
    def calculate(self, exp, index):
        deque = []
        pre = 0
        while index < len(exp) and exp[index] != ")":
            if exp[index].isdigit():
                pre = pre * 10 + int(exp[index])
                index += 1
            elif exp[index] == "(":
                res = self.calculate(exp, index + 1)
                pre = res[0]
                index = res[1] + 1
            else:
                self.getmd(deque, pre)
                deque.append(exp[index])
                pre = 0
                index += 1
        self.getmd(deque, pre)
        return [self.getsum(deque), index]

    def getmd(self, deque, pre):
        if deque and (deque[-1] == "*" or deque[-1] == "/"):
            op = deque.pop()
            v = deque.pop()
            pre = v * pre if op == "*" else v / pre
        deque.append(int(pre))

    def getsum(self, deque):
        res = 0
        isadd = True
        while deque:
            cur = deque.pop(0)
            if cur == "+":
                isadd = True
            elif cur == "-":
                isadd = False
            else:
                res += cur if isadd else -cur
        return res


if __name__ == '__main__':
    exp = input()
    test = Solution()
    print(test.calculate(exp, 0)[0])
