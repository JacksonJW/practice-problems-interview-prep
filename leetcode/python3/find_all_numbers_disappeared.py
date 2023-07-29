"""
Leetcode #448. Find All Numbers Disappeared in an Array

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), 
some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume 
the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]

Algorithm/DS used: hash table

O(n) worst case time where n is the length of the input 'nums'

O(n) worst case space where n is the length of the input 'num'

"""
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        seen_nums = {}
        for i in range(1, len(nums)+1):
            seen_nums[i] = False
        for num in nums:
            seen_nums[num] = True
        return [num for num, seen in seen_nums.items() if not seen]


def test_solution():
    s = Solution()
    print("Expected result from input [4, 3, 2, 7, 8, 2, 3, 1] is [5, 6] and the Actual result is: " +
          str(s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])))
    assert s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]


if __name__ == "__main__":
    test_solution()
