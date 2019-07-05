# Given an array nums containing n + 1 integers where each integer
# is between 1 and n(inclusive), prove that at least one duplicate
# number must exist. Assume that there is only one duplicate number,
# find the duplicate one.

# You must not modify the array(assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, but it could be repeated more than once.

# Example 1:

# Input: [1, 3, 4, 2, 2]
# Output: 2

# Example 2:

# Input: [3, 1, 3, 4, 2]
# Output: 3

# O(n*lon(n)) worst case solution (somewhat optimal):


def findDuplicate1(nums):
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return nums[i]
    return -1


# O(n) worst case time complexity most optimal solution (tortoise and hare algorithm)
def findDuplicate2(nums):
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    ptr1 = nums[0]
    ptr2 = tortoise

    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]

    return ptr1


print("O(n*log(n)) solution sorting list then seeing what is next to each number:")
print(findDuplicate1([1, 3, 4, 3, 2]))
print("O(n) solution using Floyd's Tortoise and Hare (Cycle Detection):")
print(findDuplicate2([1, 2, 2, 3, 4]))
