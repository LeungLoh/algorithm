"""
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

 

示例 1：

输入：target = 9
输出：[[2,3,4],[4,5]]
示例 2：

输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
 

限制：

1 <= target <= 10^5
"""


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        res = []
        nums = list(range(1, target // 2 + 2))
        l, r, sums = 0, 1, nums[0]
        while r < len(nums):
            sums += nums[r]
            while sums >= target:
                if sums == target:
                    res.append(nums[l:r + 1])
                sums -= nums[l]
                l += 1
            r += 1

        return res
