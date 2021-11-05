"""
Leetcode #1684 Count the Number of Consistent Strings

You are given a string allowed consisting of distinct
characters and an array of strings words. A string is
consistent if all characters in the string appear in 
the string allowed.

Return the number of consistent strings in the array words.


Example 1:
Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent
since they only contain characters 'a' and 'b'.

Example 2:
Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
Output: 7
Explanation: All strings are consistent.

Example 3:
Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
Output: 4
Explanation: Strings "cc", "acd", "ac", and "d" are consistent.

Constraints:
1 <= words.length <= 104
1 <= allowed.length <= 26
1 <= words[i].length <= 10
The characters in allowed are distinct.
words[i] and allowed contain only lowercase English letters.

Algorithm/DS used: Hashset and iteration

O(N) worst case time where N is the number of letters in list words.

O(M) worst case space where M is the length of string 'allowed'

"""
from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        result = 0
        for word in words:
            result += 1
            for letter in word:
                if letter not in allowed_set:
                    result -= 1
                    break
        return result


def test_solution():
    s = Solution()
    print("Expected result from input \"ab\", [\"ad\", \"bd\", \"aaab\", \"baa\", \"badab\"] is 2 and the Actual result is: " +
          str(s.countConsistentStrings("ab", ["ad", "bd", "aaab", "baa", "badab"])))
    assert s.countConsistentStrings(
        "ab", ["ad", "bd", "aaab", "baa", "badab"]) == 2
    assert s.countConsistentStrings(
        "abc", ["a", "b", "c", "ab", "ac", "bc", "abc"]) == 7
    assert s.countConsistentStrings(
        "cad", ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]) == 4


if __name__ == "__main__":
    test_solution()
