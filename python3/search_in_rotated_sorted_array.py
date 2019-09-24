"""
Leetcode #33 Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Algorithm/DS used: binary search modification

O(log(n)) worst case time where n is the length of the list and assuming the list is rotated sorted

O(1) worst case space

"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        stop = len(nums)-1
        midpt = (len(nums)-1) // 2
        for i in range(len(nums)-1):
            if nums[i+1] < nums[i]:
                stop = i
                start = i+1
                midpt = 0
                break

        # binary search one time but use the rules for a rotated sorted array
        if target == nums[midpt]:
            return midpt
        elif target < nums[midpt]:
            return self.binary_search(nums, target, start, len(nums)-1)
        else:
            return self.binary_search(nums, target, midpt+1, stop)

    def binary_search(self, nums, target, start, stop):
        while start <= stop:
            midpt = (start + stop)//2
            if nums[midpt] == target:
                return midpt
            elif target < nums[midpt]:
                stop = midpt-1
            else:
                start = midpt+1
        return -1


def test_solution():
    s = Solution()
    print("Expected result from input [4,5,6,7,0,1,2], target=0 is 4 and the Actual result is: " +
          str(s.search([4, 5, 6, 7, 0, 1, 2], 0)))
    assert s.search([4, 5, 6, 7, 0, 1, 2], 0) == 4

    print("Expected result from input [4, 5, 6, 7, 0, 1, 2], target = 3 is -1 and the Actual result is: " +
          str(s.search([4, 5, 6, 7, 0, 1, 2], 3)))
    assert s.search([4, 5, 6, 7, 0, 1, 2], 3) == -1


if __name__ == "__main__":
    test_solution()
