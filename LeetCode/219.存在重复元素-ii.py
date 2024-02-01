#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#
from collections import *
from typing import *
# @lc code=start


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        m = defaultdict(list)
        for i, num in enumerate(nums):
            m[num].append(i)
        for _, v in m.items():
            if len(v) < 2:
                continue
            for index in range(len(v) - 1):
                if v[index + 1] - v[index] <= k:
                    return True
        return False


test = Solution()
test.containsNearbyDuplicate([1, 2, 3, 1], 3)
# @lc code=end
