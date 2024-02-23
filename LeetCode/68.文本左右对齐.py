#
# @lc app=leetcode.cn id=68 lang=python3
#
# [68] 文本左右对齐
#
from typing import *
# @lc code=start


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line = []
        length = 0
        for i, word in enumerate(words):
            if length + len(line) + len(word) == maxWidth:
                line.append(word)
                res.append(" ".join(line))
                line[:] = []
                length = 0
            elif length + len(line) + len(word) > maxWidth:
                lack = maxWidth - length
                if len(line) > 1:
                    sp_len = lack // (len(line) - 1)
                    num = lack - sp_len * (len(line) - 1)
                    if num == 0:
                        res.append((" " * (sp_len)).join(line))
                    else:
                        res.append((" " * (sp_len + 1)).join(line[:num + 1]) + " " * (sp_len) + (" " * (sp_len)).join(line[num + 1:]))
                else:
                    res.append(line[0] + " " * lack)
                line[:] = []
                line.append(word)
                length = len(word)
            else:
                line.append(word)
                length += len(word)

        if line:
            final = " ".join(line)
            final += (maxWidth - len(final)) * " "
            res.append(final)
        return res


# test = Solution()
# print(test.fullJustify(["Science", "is", "what", "we", "understand", "well", "enough", "to",
#       "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"], 20))

# @lc code=end
