# A peak element is an element that is greater than its neighbors.

# Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

# You may imagine that nums[-1] = nums[n] = -∞.

# Example 1:

# Input: nums = [1, 2, 3, 1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
# Example 2:

# Input: nums = [1, 2, 1, 3, 5, 6, 4]
# Output: 1 or 5
# Explanation: Your function can return either index number 1 where the peak element is 2,
# or index number 5 where the peak element is 6.
# Note:

# Your solution should be in logarithmic complexity.

# My solution is logarithmic complexity


def findPeakElement(nums):
    if len(nums) == 1:
        return 0
    if len(nums) < 3:
        if nums[0] < nums[1]:
            return 1
        return 0
    return binary_search_on_peak(nums, 0, len(nums)-1)


def binary_search_on_peak(nums, l, r):
    if r <= l:
        return r
    midpt = int((r + l) / 2)
    if nums[midpt] > nums[midpt+1] and nums[midpt] > nums[midpt-1]:
        return midpt
    elif nums[midpt] < nums[midpt+1]:
        return binary_search_on_peak(nums, midpt+1, r)
    else:
        return binary_search_on_peak(nums, l, midpt-1)


print('The result expected to be 1 and the output is: ' +
      str(findPeakElement([4, 7, 5, 2, 4])))
