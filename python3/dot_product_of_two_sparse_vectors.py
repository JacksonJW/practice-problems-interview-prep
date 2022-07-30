"""
Leetcode #1570 Dot Product of Two Sparse Vectors

Given two sparse vectors, compute their dot product.

Implement class SparseVector:

SparseVector(nums) Initializes the object with the vector nums
dotProduct(vec) Compute the dot product between the instance of 
SparseVector and vec
A sparse vector is a vector that has mostly zero values, you 
should store the sparse vector efficiently and compute the dot 
product between two SparseVector.

Follow up: What if only one of the vectors is sparse?

Example 1:
Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
Output: 8
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8

Example 2:
Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
Output: 0
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0

Example 3:
Input: nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
Output: 6

Constraints:
n == nums1.length == nums2.length
1 <= n <= 10^5
0 <= nums1[i], nums2[i] <= 100

Algorithm(s)/DS used: <ALGORITHM USED/DS USED>

O(N) worst case time where N is the length of input to a 
SparseVector and input to dotProduct

O(L) worst case space where L is the length of storing only
nonzero values from the input

"""
from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.non_zero_items = {}
        for i, e in enumerate(nums):
            if e != 0:
                self.non_zero_items[i] = e

    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        is_vec_more_sparse = len(self.non_zero_items) > len(vec.non_zero_items)
        less_sparse_dict, more_sparse_dict = \
            (self.non_zero_items, vec.non_zero_items) if is_vec_more_sparse \
            else (vec.non_zero_items, self.non_zero_items)
        for key, value in more_sparse_dict.items():
            if key in less_sparse_dict:
                result += value * less_sparse_dict[key]
        return result


def test_solution():
    _v1 = SparseVector([1, 0, 0, 2, 3])
    _v2 = SparseVector([0, 3, 0, 4, 0])
    print("Expected result from input nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0] is 8 and the Actual result is: " +
          str(_v1.dotProduct(_v2)))
    assert _v1.dotProduct(_v2) == 8

    _v3 = SparseVector([0, 1, 0, 0, 0])
    _v4 = SparseVector([0, 0, 0, 0, 2])
    assert _v3.dotProduct(_v4) == 0

    _v5 = SparseVector([0, 1, 0, 0, 2, 0, 0])
    _v6 = SparseVector([1, 0, 0, 0, 3, 0, 4])
    assert _v5.dotProduct(_v6) == 6


if __name__ == "__main__":
    test_solution()
