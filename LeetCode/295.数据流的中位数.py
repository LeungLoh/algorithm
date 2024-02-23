#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#
import heapq
# @lc code=start


class MedianFinder:

    def __init__(self):
        self.heap1 = []
        self.heap2 = []

    def addNum(self, num: int) -> None:
        if not self.heap1 and not self.heap2:
            heapq.heappush(self.heap1, -num)
        elif len(self.heap1) == len(self.heap2):
            if self.heap2[0] < num:
                num = heapq.heappushpop(self.heap2, num)
            heapq.heappush(self.heap1, -num)
        elif len(self.heap1) > len(self.heap2):
            if -self.heap1[0] > num:
                num = -heapq.heappushpop(self.heap1, -num)
            heapq.heappush(self.heap2, num)
        else:
            heapq.heappush(self.heap1, -num)

    def findMedian(self) -> float:
        if len(self.heap1) == len(self.heap2):
            return (-self.heap1[0] + self.heap2[0]) / 2
        elif len(self.heap1) > len(self.heap2):
            return -self.heap1[0]
        else:
            return self.heap2[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end
