#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n - 2, -1, -1):
            temp=nums[i]
            flag=False
            for j in range(i + 1, n):
                if temp<nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]
                    flag=True
                    break
            if flag:
                break
            for j in range(i+1,n):
                nums[j-1]=nums[j]
            nums[-1]=temp


# @lc code=end
