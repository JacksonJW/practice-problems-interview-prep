# Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

# Formally the function should:

# Return true if there exists i, j, k
# such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.

# Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.


def increasing_triplet(nums):
    first = float('inf')
    second = float('inf')

    for num in nums:
        if num < first:
            first = num
        elif num < second and num > first:
            second = num
        elif num > second:
            return True
    return False


print('The list [1, 2, 3, 4, 5] should return true.')
print('result: ' + str(increasing_triplet([5, 4, 3, 2, 1])))

print('The list [5, 4, 3, 2, 1] should return false.')
print('result: ' + str(increasing_triplet([5, 4, 3, 2, 1])))
