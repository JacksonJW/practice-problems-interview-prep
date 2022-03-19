"""
Leetcode #1146 Snapshot Array

Implement a SnapshotArray that supports the following interface:

SnapshotArray(int length) initializes an array-like data 
structure with the given length.  Initially, each element equals 
0.

void set(index, val) sets the element at the given index to be 
equal to val.

int snap() takes a snapshot of the array and returns the snap_id: 
the total number of times we called snap() minus 1.

int get(index, snap_id) returns the value at the given index, at 
the time we took the snapshot with the given snap_id
 
Example 1:
Input: ["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
Output: [null,null,0,null,5]
Explanation: 
SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5);  // Set array[0] = 5
snapshotArr.snap();  // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5
 

Constraints:
1 <= length <= 50000
At most 50000 calls will be made to set, snap, and get.
0 <= index < length
0 <= snap_id < (the total number of times we call snap())
0 <= val <= 10^9

Algorithm/DS used: binary search for get(), dict for new set()'s, snap() only new set()'s

O(log(S)) worst case time for get() where S is the number of consecutive calls to set() and snap() on the same index 

O(L) worst case space where L is the size of the initialized SnapshotArray 

"""


class SnapshotArray:
    def __init__(self, length: int):
        self.set_dict = {}
        self.snap_id = -1
        self.snap_array = [[] for i in range(length)]

    def set(self, index: int, val: int) -> None:
        self.set_dict[index] = val

    def _binary_search(self, snap_array, snap_id):
        if not snap_array:
            return 0
        left, right = 0, len(snap_array)-1
        while left <= right:
            midpt = (left + right) // 2
            if snap_array[midpt][0] < snap_id:
                left = midpt + 1
            elif snap_array[midpt][0] == snap_id:
                return snap_array[midpt][1]
            else:
                right = midpt - 1
        if right == -1:
            return 0
        return snap_array[right][1]

    def snap(self) -> int:
        self.snap_id += 1
        for (index, value) in self.set_dict.items():
            self.snap_array[index].append((self.snap_id, value))
        self.set_dict = {}
        return self.snap_id

    def get(self, index: int, snap_id: int) -> int:
        return self._binary_search(self.snap_array[index], snap_id)


def test_solution():
    obj = SnapshotArray(3)
    obj.set(0, 5)
    print("Expected result from input obj.snap() is 0 and the Actual result is: " +
          str(obj.snap()))
    assert obj.snap() == 0
    obj.set(0, 6)
    print("Expected result from input obj.get(0, 0) is 5 and the Actual result is: " +
          str(obj.get(0, 0)))
    assert obj.get(0, 0) == 5


if __name__ == "__main__":
    test_solution()
