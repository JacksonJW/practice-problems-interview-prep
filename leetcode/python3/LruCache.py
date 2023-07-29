"""
Leetcode #146. LRU Cache

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

Algorithm/DS used: Ordered dictionary

O(G+P) worst case time for get and put where G is the number of times get/put is called.

O(N) worst case space where N is the amount of items inserted in the cache.

"""


from collections import deque


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.index = 0
        self.order = deque()
        self.table = {}

    def get(self, key: int) -> int:
        if key not in self.table:
            return -1
        if key in self.table:
            self.table[key][1] = self.index
            self.order.append((key, self.index))
        while self.order[0][0] == key and self.order[0][1] < self.index:
            self.order.popleft()
        self.index += 1
        return self.table[key][0]

    def put(self, key: int, value: int) -> None:
        if key in self.table:
            self.table[key][0] = value
            self.table[key][1] = self.index
            self.order.append((key, self.index))
        elif key not in self.table:
            self.table[key] = [value, self.index]
            self.order.append((key, self.index))
            if len(self.table) > self.capacity:
                while self.order[0][0] not in self.table or self.order[0][1] != self.table[self.order[0][0]][1]:
                    self.order.popleft()
                self.table.pop(self.order[0][0])
        self.index += 1


def test_solution():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1  # returns 1
    cache.put(3, 3)  # evicts key 2
    assert cache.get(2) == -1  # returns - 1 (not found)
    cache.put(4, 4)  # evicts key 1
    assert cache.get(1) == -1  # returns - 1 (not found)
    assert cache.get(3) == 3  # returns 3
    assert cache.get(4) == 4  # returns 4
    print("All tests have passed!")


if __name__ == "__main__":
    test_solution()
