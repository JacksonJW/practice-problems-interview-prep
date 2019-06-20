# Given an array of integers, find if the array contains any duplicates.

# Your function should return true if any value appears at least twice
# in the array, and it should return false if every element is distinct.


def contains_duplicate(nums):
    unique_set = set()
    for num in nums:
        if num in unique_set:
            return True
        unique_set.add(num)
    return False


print(contains_duplicate([1, 2, 3, 4, 1]))
assert contains_duplicate([1, 2, 3, 4, 1]) == True
