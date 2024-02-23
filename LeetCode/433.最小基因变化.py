#
# @lc app=leetcode.cn id=433 lang=python3
#
# [433] 最小基因变化
#
from typing import *
# @lc code=start


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if startGene == endGene:
            return 0
        if endGene not in bank:
            return -1
        queue = [startGene]
        step = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                cur = queue.pop(0)
                if cur == endGene:
                    return step
                for i, v in enumerate(cur):
                    for c in "ACGT":
                        if v == c:
                            continue
                        temp = cur[:i] + c + cur[i + 1:]
                        if temp in bank:
                            bank.remove(temp)
                            queue.append(temp)
            step += 1
        return -1


test = Solution()
print(test.minMutation("AACCGGTT", "AAACGGTA",
      ["AACCGATT", "AACCGATA", "AAACGATA", "AAACGGTA"]))
# @lc code=end

# "AACCGGTT"
# "AACCGGTA"

# AAAAACCC
# AACCCCCC
