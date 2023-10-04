"""
https://leetcode.com/problems/design-hashmap/description/?envType=daily-question&envId=2023-10-04

Example 1:

Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]



Constraints:

    0 <= key, value <= 106
    At most 104 calls will be made to put, get, and remove.

"""
class MyHashMap:

    def __init__(self):
        self.n = int(1e6+1)
        self.arr = [-1] * self.n
        

    def put(self, key: int, value: int) -> None:
        self.arr[key] = value
        

    def get(self, key: int) -> int:
        return self.arr[key]
        

    def remove(self, key: int) -> None:
        self.arr[key] = -1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
