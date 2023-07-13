#
# @lc app=leetcode.cn id=1657 lang=python3
#
# [1657] 确定两个字符串是否接近
#

# @lc code=start
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        m1 = defaultdict(int)
        m2 = defaultdict(int)
        if len(word1) != len(word2):
            return False
        for c in word1:
            m1[c] += 1
        for c in word2:
            m2[c] += 1
        for key in m1.keys():
            if key not in m2.keys():
                return False
        value1 = sorted(m1.values())
        value2 = sorted(m2.values())
        for i in range(len(value1)):
            if value1[i] != value2[i]:
                return False
        return True

# @lc code=end
