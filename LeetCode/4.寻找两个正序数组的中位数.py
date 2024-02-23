#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#
from typing import *
# @lc code=start


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length = len(nums1) + len(nums2)
        if length % 2 == 0:
            return (self.find(nums1, nums2, length // 2) + self.find(nums1, nums2, length // 2 + 1)) / 2
        else:
            return self.find(nums1, nums2, length // 2 + 1)

    def find(self, nums1, nums2, k):
        p1 = 0
        p2 = 0
        res = 0
        while k and p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                res = nums1[p1]
                p1 += 1
            else:
                res = nums2[p2]
                p2 += 1
            k -= 1
        if k == 0:
            return res
        elif p1 < len(nums1):
            return nums1[p1 + k - 1]
        else:
            return nums2[p2 + k - 1]


# test = Solution()
# print(test.find([1, 2], [3, 4], 3))


# @lc code=end
