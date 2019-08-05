"""
You're given an array of integers. Write a function that returns a pair of numbers such that they sum up to zero.

You can assume there will be exactly 1 solution. You can't use the same number twice.

Example:

Array of integers is [2, 7, 9, -2].
The pair that sums up to 0 is (2, -2).
Input:
A list of numbers, separated by space.

2 7 9 - 2
Output:
2 numbers from the array that sum up to 0.
We will sort the 2 numbers for you so that you can easily compare with our expected output.

-2 2
"""


def zero_sum(nums):
    possible_conjugates = set()
    for num in nums:
        if -num in possible_conjugates:
            return [-num, num]
        else:
            possible_conjugates.add(num)
    return None


print(zero_sum([1, 2, 3, 4]))
