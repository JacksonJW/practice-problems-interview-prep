"""
Leetcode #290 Word Pattern

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection
between a letter in pattern and a non-empty word in s.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false

Example 4:
Input: pattern = "abba", s = "dog dog dog dog"
Output: false


Constraints:
1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lower-case English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.

Algorithm/DS used: <ALGORITHM USED/DS USED>

<AVERAGE TIME COMPLEXITY> worst case time

<AVERAGE SPACE COMPLEXITY> worst case space

"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        m = {}
        letters = list(pattern)
        s = s.split()

        if len(letters) - len(s) != 0:
            return False

        for i in range(len(letters)):
            if letters[i] not in m and s[i] not in m.values():
                m[letters[i]] = s[i]
            elif letters[i] not in m and s[i] in m.values():
                return False
            elif letters[i] in m and m[letters[i]] != s[i]:
                return False
        return True


def test_solution():
    s = Solution()
    print("Expected result from input \"abba\" is \"dog cat cat dog\" and the Actual result is: " +
          str(s.wordPattern('abba', 'dog cat cat dog')))
    assert s.wordPattern('abba', 'dog cat cat dog') == True
    assert s.wordPattern('abba', 'dog cat cat fish') == False
    assert s.wordPattern('aaaa', 'dog cat cat dog') == False
    assert s.wordPattern('abba', 'dog dog dog dog') == False


if __name__ == "__main__":
    test_solution()
