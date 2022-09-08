#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#

# @lc code=start


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []
        s = [0]
        n = len(temperatures)
        res = [0] * n
        for i in range(1, n):
            while s and temperatures[i] > temperatures[s[-1]]:
                index = s.pop()
                res[index] = i - index
            s.append(i)
        return res


# @lc code=end
