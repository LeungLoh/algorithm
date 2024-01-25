#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        curlength = 0
        maxlength = 0
        length = len(nums)
        if length <= 1:
            return 0
        for i in range(length):
            maxlength = max(maxlength, i + nums[i])
            if maxlength >= length:
                return res + 1
            if i == curlength:
                curlength = maxlength
                res += 1
        return res

# @lc code=end
