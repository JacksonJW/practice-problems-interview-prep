"""
Leetcode #1512 Number of Good Pairs

Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.

Example 1:
Input: nums = [1, 2, 3, 1, 1, 3 ]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

Example 2:
Input: nums = [1, 1, 1, 1]
Output: 6
Explanation: Each pair in the array are good.

Example 3:
Input: nums = [1, 2, 3]
Output: 0
 
Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100

Algorithm/DS used: initial sort and 

O(N*log(N)) worst case time where N is the length of the input list 

<AVERAGE SPACE COMPLEXITY> worst case space

"""
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result = 0
        sorted_nums = sorted(nums)
        i = 0
        j = 1
        while i < len(nums)-1:
            if j < len(nums) and sorted_nums[i] == sorted_nums[j]:
                result += 1
                j += 1
            else:
                i += 1
                j = i + 1
        return result


def test_solution():
    s = Solution()
    print("Expected result from input [1, 2, 3, 1, 1, 3] is 4 and the Actual result is: " +
          str(s.numIdenticalPairs([1, 2, 3, 1, 1, 3])))
    assert s.numIdenticalPairs([1, 2, 3, 1, 1, 3]) == 4
    assert s.numIdenticalPairs([1, 1, 1, 1]) == 6
    assert s.numIdenticalPairs([1, 2, 3]) == 0


if __name__ == "__main__":
    test_solution()
