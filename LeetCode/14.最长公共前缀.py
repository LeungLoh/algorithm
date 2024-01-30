#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = len(strs[0])
        for s in strs:
            length = min(length, len(s))
        for index in range(length):
            flag = True
            for i in range(1, len(strs)):
                if strs[i][index] != strs[i - 1][index]:
                    flag = False
                    break
            if flag == False:
                return strs[0][:index]
        return strs[0][:length]

# @lc code=end
