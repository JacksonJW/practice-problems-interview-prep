import codewars_test as test


def solve(s):
    number_capitalized = 0
    for letter in s:
        if letter.upper() == letter:
            number_capitalized += 1
    return s.upper() if number_capitalized > len(s) // 2 else s.lower()


@test.describe("Basic tests")
def basic_tests():
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(solve("code"), "code")
        test.assert_equals(solve("CODe"), "CODE")
        test.assert_equals(solve("COde"), "code")
        test.assert_equals(solve("Code"), "code")
