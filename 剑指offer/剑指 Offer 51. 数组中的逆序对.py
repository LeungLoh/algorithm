"""
剑指 Offer 51. 数组中的逆序对
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

 

示例 1:

输入: [7,5,6,4]
输出: 5
"""


class Solution:

    def reversePairs(self, nums: List[int]) -> int:
        return self.mergesort(nums, 0, len(nums) - 1, [0] * len(nums))

    def mergesort(self, nums, l, r, tmp):
        if l >= r:
            return 0
        mid = (r + l) // 2
        res = self.mergesort(nums, l, mid, tmp) + self.mergesort(nums, mid + 1, r, tmp)
        i, j = l, mid + 1
        tmp[l:r + 1] = nums[l:r + 1]
        for k in range(l, r + 1):
            if i == mid + 1:
                nums[k] = tmp[j]
                j+=1
            elif j == r + 1 or tmp[i] <= tmp[j]:
                nums[k] = tmp[i]
                i += 1
            else:
                nums[k] = tmp[j]
                j += 1
                res += mid - i + 1
        return res