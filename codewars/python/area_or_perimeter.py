# You are given the length and width of a 4-sided polygon. The polygon can
# either be a rectangle or a square.
# If it is a square, return its area. If it is a rectangle, return its
# perimeter.

# Example(Input1, Input2 --> Output):

# 6, 10 --> 32
# 3, 3 --> 9
# Note: for the purposes of this kata you will assume that it is a square if
# its length and width are equal, otherwise it is a rectangle.
import codewars_test as test


def area_or_perimeter(l, w):
    if l == w:
        return l * w
    return 2 * l + 2 * w


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(area_or_perimeter(4, 4), 16)
        test.assert_equals(area_or_perimeter(6, 10), 32)
