#
# @lc app=leetcode.cn id=2542 lang=python3
#
# [2542] 最大子序列的分数
#

# @lc code=start
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        left = 1
        right = k + 1

        sumv = sum(nums1[:k])
        minv = min(nums2[:k])
        res = sumv * minv
        while right < len(nums1):
            sumv = sumv - nums1[left - 1] + nums1[right]
            if minv == nums2[left - 1]:
                minv = min(nums2[left:right + 1])
            else:
                minv = min(minv, nums2[right])
            res = max(res, sumv * minv)
            left += 1
            right += 1
        return res

# @lc code=end
