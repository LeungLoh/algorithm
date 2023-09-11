#
# @lc app=leetcode.cn id=2336 lang=python3
#
# [2336] 无限集中的最小数字
#

# @lc code=start
class SmallestInfiniteSet:

    def __init__(self):
       self.s=0
       self.add=set()
       
    def popSmallest(self) -> int:
        if not self.add:
            self.s+=1
            return self.s
        v=min(self.add)
        self.add.remove(v)
        return v

    def addBack(self, num: int) -> None:
        if num>self.s:
            return
        self.add.add(num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
# @lc code=end
