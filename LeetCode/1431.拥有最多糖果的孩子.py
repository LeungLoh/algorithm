#
# @lc app=leetcode.cn id=1431 lang=python3
#
# [1431] 拥有最多糖果的孩子
#

# @lc code=start
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxcandie = max(candies)
        res = []
        for item in candies:
            if item + extraCandies >= maxcandie:
                res.append(True)
            else:
                res.append(False)
        return res

# @lc code=end
