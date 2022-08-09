#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#

# @lc code=start
class MyStack:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        if not self.s1 and not self.s2:
            self.s1.append(x)
        elif not self.s1:
            self.s2.append(x)
        elif not self.s2:
            self.s1.append(x)

    def pop(self) -> int:
        if self.s1:
            for _ in range(len(self.s1) - 1):
                self.s2.append(self.s1.pop(0))
            return self.s1.pop(0)
        elif self.s2:
            for _ in range(len(self.s2) - 1):
                self.s1.append(self.s2.pop(0))
            return self.s2.pop(0)
        return -1

    def top(self) -> int:
        if self.s1:
            for _ in range(len(self.s1) - 1):
                self.s2.append(self.s1.pop(0))
            res = self.s1.pop(0)
            self.s2.append(res)
            return res
        elif self.s2:
            for _ in range(len(self.s2) - 1):
                self.s1.append(self.s2.pop(0))
            res = self.s2.pop(0)
            self.s1.append(res)
            return res
        return -1

    def empty(self) -> bool:
        if not self.s1 and not self.s2:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end
