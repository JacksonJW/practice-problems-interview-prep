# Assume the list is sorted, perform binary
# search which is takes O(log(n)) time


def binary_search(arr, l, r, num):
    if r < l:
        return -1

    midpt = int(l + (r-l) / 2)

    if arr[midpt] == num:
        return midpt

    if num < arr[midpt]:
        return binary_search(arr, l, midpt-1, num)

    return binary_search(arr, midpt+1, r, num)


def search(arr, num):
    return binary_search(arr, 0, len(arr)-1, num)


print(search([1, 2, 3, 4, 5], 1))

assert search([1, 2, 3, 4, 5], 1) == 0
