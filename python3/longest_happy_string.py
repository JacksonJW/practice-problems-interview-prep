"""
Leetcode #1405 Longest Happy String

A string s is called happy if it satisfies the following conditions:

s only contains the letters 'a', 'b', and 'c'.
s does not contain any of "aaa", "bbb", or "ccc" as a substring.
s contains at most a occurrences of the letter 'a'.
s contains at most b occurrences of the letter 'b'.
s contains at most c occurrences of the letter 'c'.

Given three integers a, b, and c, return the longest possible happy 
string. If there are multiple longest happy strings, return any of them.
If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.

Example 1:
Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.

Example 2:
Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It is the only correct answer in this case.
 

Constraints:

0 <= a, b, c <= 100
a + b + c > 0

Algorithm/DS used: Loop and look for greatest of 3 disregarding 
last letter added and add/decrement letter accordingly

O(N) worst case time where N is a+b+c

O(N) worst case space where N is a+b+c

"""


class Solution:
    def _addToResultAndDecrement(self, result, letter_count, letter,
                                 decrement_by_2):
        if letter_count > 1 and decrement_by_2:
            result += letter
            letter_count -= 1
        result += letter
        letter_count -= 1
        return (result, letter_count)

    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result = ''
        while result == '' or (result[-1] == 'a' and (b > 0 or c > 0)) \
                or (result[-1] == 'b' and (a > 0 or c > 0)) \
                or (result[-1] == 'c' and (a > 0 or b > 0)):
            if len(result) > 0:
                if result[-1] == 'a':
                    if b >= c:
                        result, b = self._addToResultAndDecrement(
                            result, b, 'b', b >= a)
                    elif c >= b:
                        result, c = self._addToResultAndDecrement(
                            result, c, 'c', c >= a)
                elif result[-1] == 'b':
                    if a >= c:
                        result, a = self._addToResultAndDecrement(
                            result, a, 'a', a >= b)
                    elif c >= a:
                        result, c = self._addToResultAndDecrement(
                            result, c, 'c', c >= b)
                elif result[-1] == 'c':
                    if a >= b:
                        result, a = self._addToResultAndDecrement(
                            result, a, 'a', a >= c)
                    elif b >= a:
                        result, b = self._addToResultAndDecrement(
                            result, b, 'b', b >= c)
            elif len(result) == 0:
                if a >= b and a >= c:
                    result, a = self._addToResultAndDecrement(
                        result, a, 'a', True)
                elif b >= a and b >= c:
                    result, b = self._addToResultAndDecrement(
                        result, b, 'b', True)
                elif c >= b and c >= a:
                    result, c = self._addToResultAndDecrement(
                        result, c, 'c', True)
        return result


def test_solution():
    s = Solution()
    print("Expected result from input  a = 1, b = 1, c = 7 is \"ccaccbcc\" and the Actual result is: " +
          str(s.longestDiverseString(1, 1, 7)))
    assert s.longestDiverseString(1, 1, 7) == 'ccaccbcc'
    assert s.longestDiverseString(7, 1, 0) == 'aabaa'
    assert s.longestDiverseString(0, 8, 11) == 'ccbccbbccbbccbbccbc'


if __name__ == "__main__":
    test_solution()
