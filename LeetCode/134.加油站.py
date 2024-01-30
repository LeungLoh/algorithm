#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#
from typing import *
# @lc code=start


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        def get_max_lentth(start_index):
            _index = start_index
            first = True
            cap = gas[start_index]
            while first or _index != start_index:
                first = False
                cap -= cost[_index]
                if cap < 0:
                    return False, _index
                _index = _index + 1 if _index < len(gas) - 1 else 0
                cap += gas[_index]
            return True, 0

        start_index = 0
        while start_index < len(gas):
            res, _index = get_max_lentth(start_index)
            if res == True:
                return start_index
            else:
                if _index + 1 <= start_index:
                    break
                else:
                    start_index = _index + 1
        return -1


# test = Solution()
# print(test.canCompleteCircuit([2, 3, 4], [3, 4, 3]))
# print(test.canCompleteCircuit([5, 8, 2, 8], [6, 5, 6, 6]))

# @lc code=end
