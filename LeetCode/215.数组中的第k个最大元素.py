#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = []
        for i in range(k):
            heapq.heappush(res, nums[i])
        for i in range(k, len(nums)):
            if res[0] < nums[i]:
                heapq.heappushpop(res, nums[i])
        return res[0]
# @lc code=end
