"""
Leetcode #151 Reverse Words in a String

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters.
The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated
by a single space.

Note that s may contain leading or trailing spaces or
multiple spaces between two words. The returned string
should only have a single space separating the words. Do 
not include any extra spaces.

Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain
leading or trailing spaces.

Example 3:
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between
two words to a single space in the reversed string.
 

Constraints:
1 <= s.length <= 104
s contains English letters (upper-case and lower-case),
digits, and spaces ' '.

There is at least one word in s.

Algorithm/DS used: Reverse iteration using split

O(N) worst case time where N is the number of words in s

O(1) worst case space

"""


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))


def test_solution():
    s = Solution()
    print("Expected result from input \"the sky is blue\" \
    is \"blue is sky the\" and the Actual result is: " +
          str(s.reverseWords("the sky is blue")))
    assert s.reverseWords("  hello world  ") == "world hello"
    assert s.reverseWords("a good   example") == "example good a"


if __name__ == "__main__":
    test_solution()
