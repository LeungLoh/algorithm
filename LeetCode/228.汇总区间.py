#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#
from typing import *
# @lc code=start


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        left = 0
        res = []
        for right in range(1, len(nums) + 1):
            if right < len(nums) and nums[right] == nums[right - 1] + 1:
                continue
            if left == right - 1:
                res.append(str(nums[left]))
                left = right
            else:
                res.append("{}->{}".format(nums[left], nums[right - 1]))
                left = right

        return res


# test = Solution()
# print(test.summaryRanges([0, 1, 2, 4, 5, 7]))

# @lc code=end
