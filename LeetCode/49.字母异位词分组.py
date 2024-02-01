#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#
from collections import *
from typing import *
# @lc code=start


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            m[key].append(s)
        return list(m.values())


test = Solution()
test.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
# @lc code=end
