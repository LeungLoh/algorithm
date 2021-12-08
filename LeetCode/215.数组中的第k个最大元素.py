#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        helper = [-num for num in nums]

        heapq.heapify(helper)

        while k - 1 and helper:
            heapq.heappop(helper)
            k -= 1
        return -helper[0]
# @lc code=end
