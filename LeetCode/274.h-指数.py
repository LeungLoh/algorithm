#
# @lc app=leetcode.cn id=274 lang=python3
#
# [274] H 指数
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations, reverse=True)
        length = len(citations)
        h = min(length, citations[0])
        while h:
            if citations[h - 1] >= h:
                return h
            h -= 1
        return h
# @lc code=end
