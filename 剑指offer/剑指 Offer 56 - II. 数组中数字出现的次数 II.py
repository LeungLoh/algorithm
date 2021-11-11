"""
在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字
示例 1：

输入：nums = [3,4,3,3]
输出：4
示例 2：

输入：nums = [9,1,7,9,7,9,7]
输出：1
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        A, B = 0, 0
        for num in nums:
            tmp = A
            A = (B & num) | (A & ~num)
            B = (B & ~num) | (~tmp & ~B & num)
        return B
