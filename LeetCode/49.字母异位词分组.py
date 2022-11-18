#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def __init__(self):
        self.paths = []

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = defaultdict(list)
        for item in strs:
            key = "".join(sorted(item))
            words[key].append(item)
        res = []
        for k, v in words.items():
            res.append(v)
        return res
# @lc code=end
