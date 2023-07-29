"""
Leetcode #706 Design HashMap

Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.

void put(int key, int value) inserts a (key, value) pair into the HashMap.
If the key already exists in the map, update the corresponding value.

int get(int key) returns the value to which the specified key is mapped,
or -1 if this map contains no mapping for the key.

void remove(key) removes the key and its corresponding value if the map
contains the mapping for the key.


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
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the
 existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
 

Constraints:
0 <= key, value <= 106
At most 104 calls will be made to put, get, and remove.

Algorithm/DS used: modulo the key value to figure out which spot in the list

O(N) worst case time where N is the number of collisions

O(M*N) worst case space where M is the size of the map_size and N is the 
number of collisions

"""


from collections import deque


class MyHashMap:

    def __init__(self):
        self.map_size = 1000
        self.map = [deque()] * self.map_size

    def put(self, key: int, value: int) -> None:
        index = key % self.map_size
        linked_list = self.map[index]
        if len(linked_list) > 0:
            found = False
            i = 0
            while not found and i < len(linked_list):
                if linked_list[i][0] == key:
                    linked_list[i][1] = value
                    found = True
                i += 1
            if not found:
                linked_list.append([key, value])
        elif len(linked_list) == 0:
            linked_list.append([key, value])

    def get(self, key: int) -> int:
        index = key % self.map_size
        linked_list = self.map[index]
        for current in linked_list:
            if current[0] == key:
                return current[1]
        return -1

    def remove(self, key: int) -> None:
        index = key % self.map_size
        linked_list = self.map[index]
        keys = [x[0] for x in linked_list]
        if key in keys:
            del linked_list[keys.index(key)]


def test_solution():
   # Your MyHashMap object will be instantiated and called as such:
    my_hash_map = MyHashMap()
    my_hash_map.put(1, 1)
    # The map is now[[1, 1]]
    my_hash_map.put(2, 2)
    # The map is now[[1, 1], [2, 2]]
    print("Expected result from input my_hash_map.get(1) is 1 and the Actual result is: " +
          str(my_hash_map.get(1)))
    assert my_hash_map.get(1) == 1
    # The map is now[[1, 1], [2, 2]]
    print("Expected result from input my_hash_map.get(3) is -1 and the Actual result is: " +
          str(my_hash_map.get(3)))
    assert my_hash_map.get(3) == -1
    # The map is now[[1, 1], [2, 2]]
    my_hash_map.put(2, 1)
    # The map is now[[1, 1], [2, 1]](i.e., update the existing value)
    print("Expected result from input my_hash_map.get(3) is 1 and the Actual result is: " +
          str(my_hash_map.get(2)))
    assert my_hash_map.get(2) == 1
    # The map is now[[1, 1], [2, 1]]
    my_hash_map.remove(2)
    # remove the mapping for 2, The map is now[[1, 1]]
    my_hash_map.get(2)
    print("Expected result from input my_hash_map.get(2) is -1 and the Actual result is: " +
          str(my_hash_map.get(2)))
    assert my_hash_map.get(2) == -1


if __name__ == "__main__":
    test_solution()
