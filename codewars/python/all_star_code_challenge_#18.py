# Create a function that accepts a string and a single character, and returns an
# integer of the count of occurrences the 2nd argument is found in the first one.

# If no occurrences can be found, a count of 0 should be returned.

# ("Hello", "o")  ==>  1
# ("Hello", "l")  ==>  2
# ("", "z")       ==>  0
# str_count("Hello", 'o'); // returns 1
# str_count("Hello", 'l'); // returns 2
# str_count("", 'z'); // returns 0

# Notes
# The first argument can be an empty string
# In languages with no distinct character data type, the second argument will be
# a string of length 1

import codewars_test as test


def str_count(strng, letter):
    count = 0
    for l in strng:
        if l == letter:
            count += 1
    return count


@test.describe("Should return the correct character count")
def fixed():
    @test.it("")
    def f():
        test.assert_equals(str_count("hello", "l"), 2)
        test.assert_equals(str_count("hello", "e"), 1)
        test.assert_equals(str_count("codewars", "c"), 1)
        test.assert_equals(str_count("ggggg", "g"), 5)
        test.assert_equals(str_count("hello world", "o"), 2)
        test.assert_equals(str_count("", "z"), 0)
