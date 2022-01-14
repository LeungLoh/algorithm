#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#

# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.QuickSort(nums, 0, len(nums) - 1)
        return nums

    def Merge(self, nums, l, r, mid):
        temp = []
        p1 = l
        p2 = mid + 1
        while p1 <= mid and p2 <= r:
            if nums[p1] < nums[p2]:
                temp.append(nums[p1])
                p1 += 1
            else:
                temp.append(nums[p2])
                p2 += 1
        if p1 <= mid:
            temp += nums[p1:mid + 1]
        if p2 <= r:
            temp += nums[p2:r + 1]
        nums[l:r + 1] = temp

    def MergeSort(self, nums, l, r):
        if r - l == 0:
            return
        if r - l == 1 and nums[r] < nums[l]:
            nums[l], nums[r] = nums[r], nums[l]
            return
        mid = l + (r - l) // 2
        self.MergeSort(nums, l, mid)
        self.MergeSort(nums, mid + 1, r)
        self.Merge(nums, l, r, mid)

    def Partition(self, nums, l, r):
        pivot = nums[r]
        p1 = l
        p2 = r
        while p1 < p2:
            while p1 < p2 and nums[p1] < pivot:
                p1 += 1
            while p1 < p2 and nums[p2] >= pivot:
                p2 -= 1
            if p1 < p2:
                nums[p1], nums[p2] = nums[p2], nums[p1]
        nums[p1], nums[r] = nums[r], nums[p1]
        return p1

    def QuickSort(self, nums, l, r):
        if l < r:
            p = self.Partition(nums, l, r)
            self.QuickSort(nums, l, p - 1)
            self.QuickSort(nums, p + 1, r)
# @lc code=end
