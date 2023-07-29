"""
Leetcode #1991 Find the Middle Index in Array

Given a 0-indexed integer array nums, find the leftmost middleIndex 
(i.e., the smallest amongst all the possible ones).

A middleIndex is an index where nums[0] + nums[1] + ... + 
nums[middleIndex-1] == nums[middleIndex+1] + nums[middleIndex+2] 
+ ... + nums[nums.length-1].

If middleIndex == 0, the left side sum is considered to be 0. 
Similarly, if middleIndex == nums.length - 1, the right side 
sum is considered to be 0.

Return the leftmost middleIndex that satisfies the condition, 
or -1 if there is no such index.

Example 1:
Input: nums = [2,3,-1,8,4]
Output: 3
Explanation:
The sum of the numbers before index 3 is: 2 + 3 + -1 = 4
The sum of the numbers after index 3 is: 4 = 4

Example 2:
Input: nums = [1,-1,4]
Output: 2
Explanation:
The sum of the numbers before index 2 is: 1 + -1 = 0
The sum of the numbers after index 2 is: 0

Example 3:
Input: nums = [2,5]
Output: -1
Explanation:
There is no valid middleIndex.

Example 4:
Input: nums = [1]
Output: 0
Explantion:
The sum of the numbers before index 0 is: 0
The sum of the numbers after index 0 is: 0

Constraints:
1 <= nums.length <= 100
-1000 <= nums[i] <= 1000

Algorithm/DS used: Running sum of leftmost and running difference of rightmost numbers

O(N) solution where N is the length of nums worst case time

O(1) worst case space since space isn't dependant on input size

"""
from typing import List


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        left = 0
        right = sum(nums)
        for i in range(len(nums)):
            right -= nums[i]
            if left == right:
                return i
            left += nums[i]
        return -1


def test_solution():
    s = Solution()
    print("Expected result from input [2, 3, -1, 8, 4] is 3 and the Actual result is: " +
          str(s.findMiddleIndex([2, 3, -1, 8, 4])))
    assert s.findMiddleIndex([2, 3, -1, 8, 4]) == 3
    assert s.findMiddleIndex([1, -1, 4]) == 2
    assert s.findMiddleIndex([2, 5]) == -1
    assert s.findMiddleIndex([1]) == 0


if __name__ == "__main__":
    test_solution()
