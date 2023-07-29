"""
Leetcode #1099 Two Sum Less Than K

Given an array nums of integers and integer k, return the maximum sum 
such that there exists i < j with nums[i] + nums[j] = sum and sum < k.
If no i, j exist satisfying this equation, return -1.

Algorithm/DS used: Brute force double for loop

O(N^2) worst case time where N is the length of nums

O(1) worst case space

"""
from typing import List


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        minimum = float('inf')
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                sum = nums[i] + nums[j]
                if sum < k:
                    minimum = min(k - sum, minimum)
        if minimum == float('inf'):
            return -1
        return k - minimum


def test_solution():
    s = Solution()
    print("Expected result from input [34,23,1,24,75,33,54,8] is 58 \
        and the Actual result is: " +
          str(s.twoSumLessThanK([34, 23, 1, 24, 75, 33, 54, 8], 60)))
    assert s.twoSumLessThanK(
        [34, 23, 1, 24, 75, 33, 54, 8], 60) == 58
    assert s.twoSumLessThanK(
        [10, 20, 30], 15) == -1


if __name__ == "__main__":
    test_solution()
