"""
Leetcode #1480 Running Sum of 1d Array

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.

Example 1:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:
Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Example 3:
Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]

Constraints:

1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6


Algorithm/DS used: Iteration

O(N) worst case time where N is the size of the input list

O(N) worst case space where N is the size of the input list

"""


"""
How to use:
- Replace class 'Solution' with your Leetcode solution.
- Replace calls 's.your_method_name()' with 's.<YOUR_ACTUAL_METHOD_NAME(<ARGS,>)>' in test_solution().
"""




from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        running_sum = []
        for num in nums:
            sum += num
            running_sum.append(sum)
        return running_sum


def test_solution():
    s = Solution()
    print("Expected result from input nums = [1, 2, 3, 4] is [1, 3, 6, 10] and the Actual result is: " +
          str(s.runningSum([1, 2, 3, 4])))
    assert s.runningSum([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert s.runningSum([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]
    assert s.runningSum([3, 1, 2, 10, 1]) == [3, 4, 6, 16, 17]


if __name__ == "__main__":
    test_solution()
