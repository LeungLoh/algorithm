#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        target = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if count == 0:
                target = nums[i]
                count += 1
            else:
                if nums[i] == target:
                    count += 1
                else:
                    count -= 1
        return target
# @lc code=end
