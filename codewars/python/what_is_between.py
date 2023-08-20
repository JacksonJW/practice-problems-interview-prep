# Complete the function that takes two integers (a, b, where a < b) and return
# an array of all integers between the input parameters, including them.

# For example:

# a = 1
# b = 4
# --> [1, 2, 3, 4]


def between(a, b):
    if b < a:
        return []
    return list(range(a, b))


import codewars_test as test


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(between(1, 4), [1, 2, 3, 4])
        test.assert_equals(between(-2, 2), [-2, -1, 0, 1, 2])
