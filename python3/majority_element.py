# Given an array of size n, find the majority element.
# The majority element is the element that appears
# more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the
# majority element always exist in the array.

# Example 1:

# Input: [3, 2, 3]
# Output: 3
# Example 2:

# Input: [2, 2, 1, 1, 1, 2, 2]
# Output: 2

# This solution is O(n) time complexity, O(n) space complexity


def majorityElement(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 1:
        return nums[0]

    count_of_nums = {}
    for num in nums:
        if num not in count_of_nums:
            count_of_nums[num] = 1
        else:
            count_of_nums[num] += 1
            if count_of_nums[num] > len(nums)//2:
                return num
