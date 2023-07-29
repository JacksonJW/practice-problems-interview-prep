"""
Leetcode #520 Detect Capital

We define the usage of capitals in a word to be right when
one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

Example 1:
Input: word = "USA"
Output: true

Example 2:
Input: word = "FlaG"
Output: false

Constraints:
1 <= word.length <= 100
word consists of lowercase and uppercase English letters.

Algorithm/DS used: Boolean logic

O(N) worst case time where N is the length of input word.

O(1) worst case space

"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper():
            return True
        elif word.islower():
            return True
        return word[0].isupper() and word[1:].islower()


def test_solution():
    s = Solution()
    print("Expected result from input 'USA' is True and the Actual result is: " +
          str(s.detectCapitalUse('USA')))
    assert s.detectCapitalUse('USA') == True
    assert s.detectCapitalUse('leetcode') == True
    assert s.detectCapitalUse('Google') == True
    assert s.detectCapitalUse('FlaG') == False


if __name__ == "__main__":
    test_solution()
