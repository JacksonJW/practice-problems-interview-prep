def singleNumber(nums):
    single_num_set = set()
    for num in nums:
        if num in single_num_set:
            single_num_set.remove(num)
        else:
            single_num_set.add(num)
    return single_num_set.pop()


print(singleNumber([4, 1, 2, 1, 2]))
assert singleNumber([4, 1, 2, 1, 2]) == 4
