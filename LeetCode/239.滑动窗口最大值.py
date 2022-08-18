#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        windows = []
        res = []
        for i in range(len(nums)):
            # 过期
            while windows and windows[0] <= i - k:
                windows.pop(0)
            while windows and nums[windows[-1]] <= nums[i]:
                windows.pop()
            windows.append(i)
            if i >= k - 1:
                res.append(nums[windows[0]])
        return res
# @lc code=end
