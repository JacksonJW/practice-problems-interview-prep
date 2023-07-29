# Count number of occurrences(or frequency) in a sorted array
# Given a sorted array arr[] and a number x, write a function
# that counts the occurrences of x in arr[].

# Expected time complexity is O(Logn)


def find_frequency(arr, num):
    index = binary_search(arr, 0, len(arr)-1, num)
    return count_occurrences_left_and_right(index, arr, num)


def binary_search(arr, l, r, num):
    if r < l:
        return -1

    midpt = int(l + (r - l) / 2)

    if num == arr[midpt]:
        return midpt

    if num < arr[midpt]:
        return binary_search(arr, l, midpt-1, num)

    return binary_search(arr, midpt+1, r, num)


def count_occurrences_left_and_right(index, arr, num):
    if index == -1:
        return 0

    # check left
    count = 1
    left = index-1
    while left >= 0 and arr[left] == num:
        count += 1
        left -= 1

    # check right
    right = index+1
    while right < len(arr) and arr[right] == num:
        count += 1
        right += 1

    return count


print(find_frequency([1, 2, 2, 2, 3, 4, 5], 2))
