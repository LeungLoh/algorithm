#
# @lc app=leetcode.cn id=373 lang=python3
#
# [373] 查找和最小的 K 对数字
#

# @lc code=start
import heapq
from collections import *
from typing import *


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans = []
        heap = [(nums1[i] + nums2[0], i, 0) for i in range(min(k, len(nums1)))]
        while heap and len(ans) < k:
            _, i, j = heapq.heappop(heap)
            ans.append((nums1[i], nums2[j]))
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return ans


test = Solution()
print(test.kSmallestPairs([1, 7, 11], [2, 4, 6], 3))
print(test.kSmallestPairs([1, 2, 4, 5, 6], [3, 5, 7, 9], 20))
# @lc code=end
