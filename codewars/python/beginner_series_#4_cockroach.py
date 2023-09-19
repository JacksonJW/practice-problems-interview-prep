# The cockroach is one of the fastest insects. Write a function which takes its
# speed in km per hour and returns it in cm per second, rounded down to the
# integer (= floored).

# For example:

# 1.08 --> 30
# Note! The input is a Real number (actual type is language dependent) and is
# >= 0. The result should be an Integer.

import math
import codewars_test as test


def cockroach_speed(s):
    return math.floor(s * 100000 / 3600)


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(cockroach_speed(1.08), 30)
        test.assert_equals(cockroach_speed(1.09), 30)
        test.assert_equals(cockroach_speed(0), 0)
