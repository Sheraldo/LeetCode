"""
https://leetcode.com/problems/lru-cache/description/

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
"""
class LRUCache:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.n = None
            self.p = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1)
        self.head.n = self.tail
        self.tail.p = self.head
        self.cache = {}

    def delete_node(self, curr):
        prv = curr.p
        nxt = curr.n
        prv.n = nxt
        nxt.p = prv
        curr.p, curr.n = None, None
        k = curr.key
        del curr
        del self.cache[k]


    def insert(self, key, value):
        if self.capacity == len(self.cache) and self.head.n != self.tail:
            self.delete_node(self.head.n)
        nn = self.Node(key, value)
        nn.n = self.tail
        nn.p = self.tail.p
        self.tail.p.n = nn
        self.tail.p = nn
        self.cache[key] = nn

    def get(self, key: int) -> int:
        if key in self.cache:
            value = self.cache[key].value
            self.delete_node(self.cache[key])
            self.insert(key, value)
            return value
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete_node(self.cache[key])
        self.insert(key, value)
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
