# Task
# Given an array of integers, remove the smallest value. Do not mutate the
# original array/list. If there are multiple elements with the same value,
# remove the one with a lower index. If you get an empty array/list, return an
# empty array/list.

# Don't change the order of the elements that are left.

# Examples
# * Input: [1,2,3,4,5], output = [2,3,4,5]
# * Input: [5,3,2,1,4], output = [5,3,2,4]
# * Input: [2,2,1,2,1], output = [2,2,2,1]

import codewars_test as test


def remove_smallest(numbers):
    if not numbers:
        return []
    result = []
    minimum = min(numbers)
    seen_minimum = False
    for number in numbers:
        if number == minimum and seen_minimum is False:
            seen_minimum = True
        else:
            result.append(number)
    return result


test.describe("remove_smallest")

test.it("works for the examples")
test.assert_equals(
    remove_smallest([1, 2, 3, 4, 5]), [2, 3, 4, 5], "Wrong result for [1, 2, 3, 4, 5]"
)
test.assert_equals(
    remove_smallest([5, 3, 2, 1, 4]), [5, 3, 2, 4], "Wrong result for [5, 3, 2, 1, 4]"
)
test.assert_equals(
    remove_smallest([1, 2, 3, 1, 1]), [2, 3, 1, 1], "Wrong result for [1, 2, 3, 1, 1]"
)
test.assert_equals(remove_smallest([]), [], "Wrong result for []")

from numpy.random import randint


def randlist():
    return list(randint(400, size=randint(1, 10)))


test.it("returns [] if list has only one element")
for i in range(10):
    x = randint(1, 400)
    test.assert_equals(remove_smallest([x]), [], "Wrong result for [{}]".format(x))

test.it("returns a list that misses only one element")
for i in range(10):
    arr = randlist()
    test.assert_equals(
        len(remove_smallest(arr[:])),
        len(arr) - 1,
        "Wrong sized result for {}".format(arr),
    )
