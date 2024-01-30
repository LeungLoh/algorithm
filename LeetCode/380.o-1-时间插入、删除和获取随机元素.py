#
# @lc app=leetcode.cn id=380 lang=python3
#
# [380] O(1) 时间插入、删除和获取随机元素
#

# @lc code=start
class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.m = {}

    def insert(self, val: int) -> bool:
        if self.m.get(val) != None:
            return False
        self.nums.append(val)
        self.m[val] = len(self.nums) - 1

    def remove(self, val: int) -> bool:
        if self.m.get(val) == None:
            return False
        index = self.m[val]
        self.nums[index] = self.nums[-1]
        self.m[self.nums[index]] = index
        self.nums.pop()
        del self.m[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end
