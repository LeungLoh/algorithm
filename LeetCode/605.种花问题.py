#
# @lc app=leetcode.cn id=605 lang=python3
#
# [605] 种花问题
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # def canPlaceFlowers(self, flowerbed, n):
        flowerbed = [0] + flowerbed + [0]
        p1 = 0
        p2 = 0
        while p1 < len(flowerbed) and p2 < len(flowerbed):
            while p1 < len(flowerbed) and flowerbed[p1] == 1:
                p1 += 1
            p2 = p1 + 1
            while p2 < len(flowerbed) and flowerbed[p2] == 0:
                p2 += 1
            length = p2 - p1 + 1
            n -= length // 2 - 1
            p1 = p2 + 1
        if n <= 0:
            return True
        return False


# test = Solution()
# print(test.canPlaceFlowers([1, 0, 0, 0, 1, 0, 0], 2))


# @lc code=end
