"""
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

 

示例 1：

输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]
示例 2：

输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]
 

限制：

2 <= nums.length <= 10000
"""


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        nxor = nums[0]
        res = [0, 0]
        for i in range(1, len(nums)):
            nxor ^= nums[i]
        k = 1
        while nxor & k == 0:
            k <<= 1

        for num in nums:
            if num & k == 0:
                res[0] ^= num
            else:
                res[1] ^= num
        return res
