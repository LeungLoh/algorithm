#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#

# @lc code=start


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        m = {0: 1}
        sums = 0
        ans = 0
        for num in nums:
            sums += num
            if sums - k in m.keys():
                ans += m[sums - k]

            m[sums] = m.get(sums, 0) + 1
        return ans

# @lc code=end
