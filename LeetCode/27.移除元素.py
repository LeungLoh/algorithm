#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i, v in enumerate(nums):
            if v != val:
                nums[index] = nums[i]
                index += 1
        return index

# @lc code=end
