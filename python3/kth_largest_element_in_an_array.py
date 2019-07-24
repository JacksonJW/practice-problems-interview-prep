def findKthLargest(nums, k):
    nums.append(float('inf'))
    return partition(nums, 0, len(nums)-1, k)


def partition(nums, left, right, k):
    if left == right:
        return nums[left]
    i = left
    j = right
    pivot_index = i
    pivot = nums[i]
    n = len(nums)

    while i < j:

        while True:
            i += 1
            if nums[i] > pivot:
                break

        while True:
            j -= 1
            if nums[j] <= pivot:
                break

        if i < j:
            nums[i], nums[j] = nums[j], nums[i]

    nums[j], nums[pivot_index] = nums[pivot_index], nums[j]

    if n - k - 1 == j:
        return nums[j]
    elif n - k - 1 < j:
        return partition(nums, left, j, k)
    else:
        return partition(nums, j+1, right, k)


print('the expected result should be 5 and the actual result is: ' +
      str(findKthLargest([3, 2, 1, 5, 6, 4], 2)))
