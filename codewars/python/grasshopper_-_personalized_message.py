import codewars_test as test


def greet(name, owner):
    if name == owner:
        return "Hello boss"
    else:
        return "Hello guest"


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(greet("Daniel", "Daniel"), "Hello boss")
        test.assert_equals(greet("Greg", "Daniel"), "Hello guest")
