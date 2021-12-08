#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length = len(nums1) + len(nums2)
        if length % 2 == 0:
            return (self.findnums(nums1, nums2, length // 2) + self.findnums(nums1, nums2, length // 2 + 1)) / 2
        else:
            return self.findnums(nums1, nums2, length // 2 + 1)

    def findnums(self, nums1, nums2, k):
        if k == 1:
            if not nums1:
                return nums2[0]
            if not nums2:
                return nums1[0]
            return min(nums1[0], nums2[0])
        if not nums1:
            return self.findnums(nums1, nums2[1:], k - 1)
        if not nums2:
            return self.findnums(nums1[1:], nums2, k - 1)
        if nums1[0] < nums2[0]:
            return self.findnums(nums1[1:], nums2, k - 1)
        else:
            return self.findnums(nums1, nums2[1:], k - 1)


# @lc code=end
