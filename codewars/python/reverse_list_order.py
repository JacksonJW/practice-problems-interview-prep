# In this kata you will create a function that takes in a list and returns a
# list with the reverse order.

# Examples (Input -> Output)
# * [1, 2, 3, 4]  -> [4, 3, 2, 1]
# * [9, 2, 0, 7]  -> [7, 0, 2, 9]


import codewars_test as test


def reverse_list(l):
    return list(reversed(l))


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(reverse_list([1, 2, 3, 4]), [4, 3, 2, 1])
        test.assert_equals(reverse_list([3, 1, 5, 4]), [4, 5, 1, 3])
        test.assert_equals(reverse_list([3, 6, 9, 2]), [2, 9, 6, 3])
        test.assert_equals(reverse_list([1]), [1])
