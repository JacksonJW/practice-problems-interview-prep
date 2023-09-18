# Make a function that returns the value multiplied by 50 and increased by 6.
# If the value entered is a string it should return "Error".

import codewars_test as test


def problem(a):
    if isinstance(a, str):
        return "Error"
    return a * 50 + 6


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(problem("hello"), "Error")
        test.assert_equals(problem(1), 56)
