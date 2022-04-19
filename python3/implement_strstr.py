"""
Leetcode #28. Implement strStr()

Implement strStr().

Given two strings needle and haystack, return the index of the first 
occurrence of needle in haystack, or -1 if needle is not part of 
haystack.

Clarification:
What should we return when needle is an empty string? This is a great
question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an
empty string. This is consistent to C's strstr() and Java's indexOf().

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Constraints:
1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.

Algorithm/DS used: using python3's .index function

O(N) worst case time where N is the length of haystack

O(1) worst case space

"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        try:
            return haystack.index(needle)
        except ValueError:
            return -1


def test_solution():
    s = Solution()
    print("Expected result from input haystack = \"mississippi\" \
    needle = \"issip\" is 4 and the Actual result is : " +
          str(s.strStr("mississippi", "issip")))
    assert s.strStr("mississippi", "issip") == 4
    assert s.strStr("aaaaa", "bba") == -1
    assert s.strStr("hello", "ll") == 2


if __name__ == "__main__":
    test_solution()
