#
# @lc app=leetcode.cn id=1109 lang=python3
#
# [1109] 航班预订统计
#

# @lc code=start
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] * n
        for booking in bookings:
            res[booking[0] - 1] += booking[2]
            if booking[1] < n:
                res[booking[1]] -= booking[2]
        for i in range(1, n):
            res[i] += res[i - 1]
        return res

# @lc code=end