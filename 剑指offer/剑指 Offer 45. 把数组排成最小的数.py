"""
输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。

 

示例 1:

输入: [10,2]
输出: "102"
示例 2:

输入: [3,30,34,5,9]
输出: "3033459"
"""


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        res = [str(item)for item in nums]
        res = sorted(res, key=cmp_to_key(lambda x, y: 1 if x + y > y + x else -1))
        return "".join(res)
