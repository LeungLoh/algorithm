#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
import heapq
from multiprocessing import heap
import re


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        res = []
        for num in nums:
            m[num] = m.get(num, 0) + 1
        for key, v in m.items():
            res.append((key, v))
        res = sorted(res, key=lambda x: x[1], reverse=True)
        res = [item[0] for item in res[:k]]
        return res

# @lc code=end
