# Take 2 strings s1 and s2 including only letters from a to z. Return a new
# sorted string, the longest possible, containing distinct letters - each taken
# only once - coming from s1 or s2.

# Examples:
# a = "xyaabbbccccdefww"
# b = "xxxxyyyyabklmopq"
# longest(a, b) -> "abcdefklmopqwxy"

# a = "abcdefghijklmnopqrstuvwxyz"
# longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

import codewars_test as test


def longest(a1, a2):
    distinct_set = set(a1 + a2)
    return "".join(sorted(list(distinct_set)))


@test.describe("longest")
def tests():
    @test.it("basic tests")
    def basics():
        test.assert_equals(longest("aretheyhere", "yestheyarehere"), "aehrsty")
        test.assert_equals(
            longest("loopingisfunbutdangerous", "lessdangerousthancoding"),
            "abcdefghilnoprstu",
        )
        test.assert_equals(
            longest("inmanylanguages", "theresapairoffunctions"), "acefghilmnoprstuy"
        )
