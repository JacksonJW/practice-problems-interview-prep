# Complete the function/method so that it returns the url with anything after
# the anchor (#) removed.

# Examples
# "www.codewars.com#about" --> "www.codewars.com"
# "www.codewars.com?page=1" -->"www.codewars.com?page=1"

import codewars_test as test


def remove_url_anchor(url):
    result = ""
    for c in url:
        if c == "#":
            return result
        result += c
    return result


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(
            remove_url_anchor("www.codewars.com#about"), "www.codewars.com"
        )
        test.assert_equals(
            remove_url_anchor("www.codewars.com/katas/?page=1#about"),
            "www.codewars.com/katas/?page=1",
        )
        test.assert_equals(
            remove_url_anchor("www.codewars.com/katas/"), "www.codewars.com/katas/"
        )
