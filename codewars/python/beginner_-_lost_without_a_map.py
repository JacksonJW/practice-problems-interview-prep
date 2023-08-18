# Given an array of integers, return a new array with each value doubled.

import codewars_test as test


def maps(a):
    return [2 * number for number in a]


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(maps([1, 2, 3]), [2, 4, 6])
        test.assert_equals(
            maps([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
        )
        test.assert_equals(maps([]), [])
