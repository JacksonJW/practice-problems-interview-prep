# Now you have to write a function that takes an argument and returns the
# square of it.


import codewars_test as test


def square(n):
    return n**2


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(square(2), 4)
        test.assert_equals(square(50), 2500)
        test.assert_equals(square(1), 1)
