#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = sys.maxsize
        for s in strs:
            length = min(length, len(s))

        for i in range(length):
            for j in range(1, len(strs)):
                if strs[j][i] != strs[j - 1][i]:
                    return strs[0][:i]
        return strs[0][:length]
# @lc code=end
