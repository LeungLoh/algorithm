#
# @lc app=leetcode.cn id=733 lang=python3
#
# [733] 图像渲染
#

# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.dfs(image, sr, sc, image[sr][sc], newColor)
        return image

    def dfs(self, image, x, y, oldColor, newColor):
        if x < 0 or x >= len(image) or y < 0 or y >= len(image[0]):
            return
        if image[x][y] != oldColor or image[x][y] == newColor:
            return
        image[x][y] = newColor
        self.dfs(image, x - 1, y, oldColor, newColor)
        self.dfs(image, x + 1, y, oldColor, newColor)
        self.dfs(image, x, y - 1, oldColor, newColor)
        self.dfs(image, x, y + 1, oldColor, newColor)
# @lc code=end
