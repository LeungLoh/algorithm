#
# @lc app=leetcode.cn id=443 lang=python3
#
# [443] 压缩字符串
#

# @lc code=start
class Solution:
    def compress(self, chars: List[str]) -> int:
        # def compress(self, chars):
        p1 = 0
        p2 = p1 + 1
        n = len(chars)
        new_length = 0
        while p1 < n:
            while p2 < n and chars[p1] == chars[p2]:
                p2 += 1
            length = p2 - p1
            chars[new_length] = chars[p1]
            new_length += 1
            if length > 1:
                for d in str(length):
                    chars[new_length] = d
                    new_length += 1

            p1 = p2
            p2 += 1

        chars = chars[:new_length]

        return new_length


# test = Solution()
# print(test.compress(["a", "a", "b", "b", "c", "c", "c"]))

# @lc code=end
