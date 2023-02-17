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
        if key in self.buffer:
            node = self.buffer[key]
            self.remove(node)
            self.add(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.buffer:
            self.remove(self.buffer[key])
        elif len(self.buffer) == self.cap:
            self.remove(self.head.next)
            del self.buffer[self.head.next]

        self.add(Node(key, value))
        self.buffer[key] = Node(key, value)

    def add(self, node):
        pre = self.tail.prev
        node.prev = pre
        pre.next = node
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        node.next.pre = node.pre
        node.pre.next = node.next


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
