#
# @lc app=leetcode.cn id=1207 lang=python3
#
# [1207] 独一无二的出现次数
#

# @lc code=start
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        map = defaultdict(int)
        for num in arr:
            map[num] += 1
        if len(map.values()) != len(set(map.values())):
            return False
        return True
# @lc code=end
