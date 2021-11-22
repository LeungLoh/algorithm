#
# @lc app=leetcode.cn id=384 lang=python3
#
# [384] 打乱数组
#

# @lc code=start
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = copy.deepcopy(nums)
        self.cur = copy.deepcopy(nums)

    def reset(self) -> List[int]:
        self.cur = copy.deepcopy(self.nums)
        return self.cur

    def shuffle(self) -> List[int]:
        for i in range(len(self.cur)):
            index = random.randint(0, len(self.cur) - 1)
            self.cur[i], self.cur[index] = self.cur[index], self.cur[i]
        return self.cur


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
# @lc code=end
