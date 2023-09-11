#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        right = len(nums) - 1
        left = 0
        while left <= right:

            while nums[left] == val:
                if left == right:
                    if nums[left] == val:
                        return left
                    else:
                        return left + 1
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            left += 1
        return left
# @lc code=end
