def product(arr, index):
    product = 1
    for i in range(len(arr)):
        if i != index:
            product *= arr[i]
    return product


print(product([1, 2, 3, 4, 5], 2))
assert product([1, 2, 3, 4, 5], 2) == 40
