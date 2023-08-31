# In this simple exercise, you will create a program that will take two lists of
# integers, a and b. Each list will consist of 3 positive integers above 0,
# representing the dimensions of cuboids a and b. You must find the difference of
# the cuboids' volumes regardless of which is bigger.

# For example, if the parameters passed are ([2, 2, 3], [5, 4, 1]), the volume
# of a is 12 and the volume of b is 20. Therefore, the function should return 8.

# Your function will be tested with pre-made examples as well as random ones.

# If you can, try writing it in one line of code.

import codewars_test as test


def find_difference(a, b):
    a_product = 1
    b_product = 1
    for number in a:
        a_product *= number
    for number in b:
        b_product *= number
    return abs(a_product - b_product)


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(
            find_difference([3, 2, 5], [1, 4, 4]),
            14,
            "{0} should equal 14".format(find_difference([3, 2, 5], [1, 4, 4])),
        )
        test.assert_equals(
            find_difference([9, 7, 2], [5, 2, 2]),
            106,
            "{0} should equal 106".format(find_difference([9, 7, 2], [5, 2, 2])),
        )
        test.assert_equals(
            find_difference([11, 2, 5], [1, 10, 8]),
            30,
            "{0} should equal 30".format(find_difference([11, 2, 5], [1, 10, 8])),
        )
        test.assert_equals(
            find_difference([4, 4, 7], [3, 9, 3]),
            31,
            "{0} should equal 31".format(find_difference([4, 4, 7], [3, 9, 3])),
        )
        test.assert_equals(
            find_difference([15, 20, 25], [10, 30, 25]),
            0,
            "{0} should equal 0".format(find_difference([15, 20, 25], [10, 30, 25])),
        )


@test.describe("Random Tests:")
def random_tests():
    from random import randint
    from functools import reduce

    for x in range(50):
        a = [randint(1, 30), randint(1, 30), randint(1, 30)]
        b = [randint(1, 30), randint(1, 30), randint(1, 30)]
        expected = abs(reduce(lambda x, y: x * y, a) - reduce(lambda x, y: x * y, b))

        @test.it(f"testing for find_difference({a}, {b})")
        def test_case():
            test.assert_equals(find_difference(a, b), expected)
