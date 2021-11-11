"""
从若干副扑克牌中随机抽 5 张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

 

示例 1:

输入: [1,2,3,4,5]
输出: True
 

示例 2:

输入: [0,0,1,2,5]
输出: True
"""


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        zeronums = 1 if nums[0] == 0 else 0
        for i in range(1, len(nums)):
            if nums[i] == 0:
                zeronums += 1
                continue
            if zeronums < 0:
                return False
            if nums[i] == nums[i - 1]:
                return False
            if nums[i - 1] == 0:
                continue
            zeronums -= nums[i] - nums[i - 1] - 1

        return True if zeronums >= 0 else False
