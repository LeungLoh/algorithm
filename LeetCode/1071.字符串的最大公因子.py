#
# @lc app=leetcode.cn id=1071 lang=python3
#
# [1071] 字符串的最大公因子
#

# @lc code=start
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        pattern = ""
        length = len(str2)
        for i in range(length):
            if str1[i] == str2[i]:
                pattern += str1[i]
            else:
                break
        while pattern:
            if self.check(str1, pattern) and self.check(str2, pattern):
                return pattern
            pattern = pattern[:-1]
        return ""

    def check(self, str1, str2):
        length = len(str2)
        res = [str1[i:i + length] for i in range(0, len(str1), length)]
        res = list(set(res))
        if len(res) == 1 and res[0] == str2:
            return True
        return False


test = Solution()
print(test.gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"))

# @lc code=end
