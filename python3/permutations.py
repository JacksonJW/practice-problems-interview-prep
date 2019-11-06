import itertools
from typing import List
"""
Leetcode #46. Permutations

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

Algorithm/DS used: permutations

O(n!) worst case time where n is the length of "nums" - the input list

O(n) worst case space where n is the length of nums

"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums, len(nums)))


def test_solution():
    s = Solution()
    print("Expected result from input [1, 2, 3] is [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)] and the Actual result is: " +
          str(s.permute([1, 2, 3])))
    assert s.permute([1, 2, 3]) == [(1, 2, 3), (1, 3, 2), (
        2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]


if __name__ == "__main__":
    test_solution()
