#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存机制
#

# @lc code=start


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.buffer = {}

    def get(self, key: int) -> int:
        node = self.buffer.get(key)
        if node:
            self.remove(node)
            self.add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        node = self.buffer.get(key)
        if node:
            self.remove(node)
        elif len(self.buffer) == self.cap:
            del self.buffer[self.head.next.key]
            self.remove(self.head.next)

        node = Node(key, value)
        self.add(node)
        self.buffer[key] = node

    def add(self, node):
        pre = self.tail.prev
        pre.next = node
        node.prev = pre
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        node.prev = None
        node.next = None

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
