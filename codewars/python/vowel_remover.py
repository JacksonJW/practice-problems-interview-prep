# Create a function called shortcut to remove the lowercase vowels
# (a, e, i, o, u ) in a given string.

# Examples
# "hello"     -->  "hll"
# "codewars"  -->  "cdwrs"
# "goodbye"   -->  "gdby"
# "HELLO"     -->  "HELLO"
# don't worry about uppercase vowels
# y is not considered a vowel for this kata
import codewars_test as test


def shortcut(s):
    result = ""
    vowels = set("aeiou")
    for letter in s:
        if letter not in vowels:
            result = result + letter
    return result


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Test Cases")
    def basic_test_cases():
        test.assert_equals(shortcut("hello"), "hll")
        test.assert_equals(shortcut("hellooooo"), "hll")
        test.assert_equals(shortcut("how are you today?"), "hw r y tdy?")
        test.assert_equals(shortcut("complain"), "cmpln")
        test.assert_equals(shortcut("never"), "nvr")
