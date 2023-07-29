# Given an array nums, write a function to move all 0's
# to the end of it while maintaining the relative order
# of the non-zero elements.

# solution is O(n) (somewhat suboptimal) time complexity and O(1) space


def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    count = 0
    for num in nums:
        if num == 0:
            count += 1

    i = 0
    j = 1
    while i < len(nums) - count:
        if nums[i] == 0:
            while i < len(nums) - count:
                if nums[j] != 0:
                    nums[i] = nums[j]
                    i += 1
                j += 1
            break
        i += 1
        j += 1

    while i < len(nums):
        nums[i] = 0
        i += 1


nums = [0, 0, 1, 2, 3, 4]
print("input is: " + str(nums))
moveZeroes(nums)
assert nums == [1, 2, 3, 4, 0, 0]
print("output is " + str(nums))
