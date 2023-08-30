import codewars_test as test


def number_to_string(num):
    return str(num)


@test.describe("Fixed Tests")
def basic_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(number_to_string(67), "67")
        test.assert_equals(number_to_string(79585), "79585")
        test.assert_equals(number_to_string(79585), "79585")
        test.assert_equals(number_to_string(1 + 2), "3")
        test.assert_equals(number_to_string(1 - 2), "-1")
