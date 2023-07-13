#
# @lc app=leetcode.cn id=841 lang=python3
#
# [841] 钥匙和房间
#
from typing import *
# @lc code=start


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [0] * len(rooms)
        visited[0] = 1
        keys = rooms[0]
        while keys:
            key = keys.pop(0)
            if visited[key] == 0:
                visited[key] = 1
                keys += rooms[key]

        for item in visited:
            if item == 0:
                return False
        return True


test = Solution()
print(test.canVisitAllRooms([[1], [2], [3], []]))
# @lc code=end
