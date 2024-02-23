#
# @lc app=leetcode.cn id=502 lang=python3
#
# [502] IPO
#
import heapq
# @lc code=start

from typing import *


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap = []
        for i in range(len(profits)):
            heapq.heappush(heap, (-profits[i], capital[i]))

        for _ in range(k):
            temp = []
            while heap and w < heap[0][1]:
                temp.append(heapq.heappop(heap))
            if not heap:
                break
            pv = heapq.heappop(heap)
            w -= pv[0]
            for item in temp:
                heapq.heappush(heap, item)
        return w


test = Solution()
test.findMaximizedCapital(1, 0, [1, 2, 3], [1, 1, 2])
# @lc code=end
