"""
请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。

若队列为空，pop_front 和 max_value 需要返回 -1

示例 1：

输入:
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]
示例 2：

输入:
["MaxQueue","pop_front","max_value"]
[[],[],[]]
输出: [null,-1,-1]
"""
from _typeshed import Self


class MaxQueue:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def max_value(self) -> int:
        return self.queue2[0] if self.queue2 else -1

    def push_back(self, value: int) -> None:
        while self.queue2 and self.queue2[-1] < value:
            self.queue2.pop()
        self.queue1.append(value)
        self.queue2.append(value)

    def pop_front(self) -> int:
        if not self.queue1:
            return -1
        res = self.queue1[0]
        self.queue1.pop(0)
        if res == self.queue2[0]:
            self.queue2.pop(0)
        return res

# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
