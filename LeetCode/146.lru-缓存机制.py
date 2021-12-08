#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存机制
#

# @lc code=start
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.queue = []

    def get(self, key: int) -> int:
        if self.cache.get(key) != None:
            self.queue.remove(key)
            self.queue.insert(0, key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.cache.get(key) != None:
            self.queue.remove(key)
        elif len(self.queue) >= self.cap:
            index = self.queue.pop()
            self.cache.pop(index)
        self.cache[key] = value
        self.queue.insert(0, key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
