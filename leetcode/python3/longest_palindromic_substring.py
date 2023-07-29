"""
Leetcode #5 Longest Palindromic Substring

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

Algorithm/DS used: Sliding window

O(n^2) worst case time

O(1) worst case space

"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        longest_palindrome = ""

        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                longest_palindrome = self.expand_center(
                    s, i, i+1, longest_palindrome)

        for j in range(len(s)-2):
            if s[j] == s[j+2]:
                longest_palindrome = self.expand_center(
                    s, j, j+2, longest_palindrome)

        return longest_palindrome

    def expand_center(self, s: str, left: int, right: int, longest_palindrome: str) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > len(longest_palindrome):
                longest_palindrome = s[left:right+1]
            left -= 1
            right += 1
        return longest_palindrome


def test_solution():
    s = Solution()
    print("Expected result from input \"babad\" is \"aba\" or \"bab\" and the Actual result is: " +
          str(s.longestPalindrome("babad")))
    print("Expected result from input \"cbbd\" is \"bb\" and the Actual result is: " +
          str(s.longestPalindrome("cbbd")))
    assert s.longestPalindrome("babad") == "bab"
    assert s.longestPalindrome("cbbd") == "bb"


if __name__ == "__main__":
    test_solution()
