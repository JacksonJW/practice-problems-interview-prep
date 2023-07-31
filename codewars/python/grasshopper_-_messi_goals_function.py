import codewars_test as test


def goals(laLiga, copaDelRey, championsLeague):
    return laLiga + copaDelRey + championsLeague


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(goals(0, 0, 0), 0)
        test.assert_equals(goals(5, 10, 2), 17)
