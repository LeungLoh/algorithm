#
# @lc app=leetcode.cn id=649 lang=python3
#
# [649] Dota2 参议院
#

# @lc code=start
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue1 = [item for item in senate]
        queue2 = []
        while queue1:
            cur = queue1.pop(0)
            if not queue2 or queue2[0] == cur:
                queue2.append(cur)
            else:
                queue1.append(queue2.pop(0))
        if queue2[0] == "R":
            return "Radiant"
        else:
            return "Dire"


# @lc code=end
