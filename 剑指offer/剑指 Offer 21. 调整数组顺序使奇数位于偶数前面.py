"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数在数组的前半部分，所有偶数在数组的后半部分。

 

示例：

输入：nums = [1,2,3,4]
输出：[1,3,2,4] 
注：[3,1,2,4] 也是正确的答案之一。
"""


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[l] % 2 == 0:
                while l < r and nums[r] % 2 == 0:
                    r -= 1
                nums[l], nums[r] = nums[r], nums[l]
            l += 1
        return nums
