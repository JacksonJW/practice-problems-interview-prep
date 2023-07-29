"""
Leetcode #704 Binary Search

Given a sorted (in ascending order) integer array nums of n elements and a target value, 
write a function to search target in nums. If target exists, then return its index, 
otherwise return -1.


Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Note:

You may assume that all elements in nums are unique.
n will be in the range [1, 10000].
The value of each element in nums will be in the range [-9999, 9999].

Algorithm/DS used: O(n)

O(log(n)) worst case time where n is the length of the list 'nums'

O(1) worst case space

"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self._binary_search(nums, target, 0, len(nums)-1)

    def _binary_search(self, nums, target, start, end):
        if start > end:
            return -1

        midpt = (start + end + 1) // 2

        if target == nums[midpt]:
            return midpt
        elif target < nums[midpt]:
            return self._binary_search(nums, target, start, midpt-1)
        else:
            return self._binary_search(nums, target, midpt+1, end)


def test_solution():
    s = Solution()
    print("Expected result from input nums = [-1,0,3,5,9,12], target = 9 is 4 and the Actual result is: " +
          str(s.search([-1, 0, 3, 5, 9, 12], 9)))
    assert s.search([-1, 0, 3, 5, 9, 12], 9) == 4
    print("Expected result from input nums = [-1,0,3,5,9,12], target = 2 is -1 and the Actual result is: " +
          str(s.search([-1, 0, 3, 5, 9, 12], 2)))
    assert s.search([-1, 0, 3, 5, 9, 12], 2) == -1


if __name__ == "__main__":
    test_solution()
