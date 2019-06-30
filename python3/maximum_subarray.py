# Given an integer array nums, find the contiguous
# subarray(containing at least one number)
# which has the largest sum and return its sum.

# Example:

# Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4],
# Output: 6
# Explanation: [4, -1, 2, 1] has the largest sum = 6.


def max_subarray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    for i in range(len(nums)-1):
        if nums[i] > 0:
            nums[i+1] = nums[i] + nums[i+1]

    return max(nums)
