"""
Leetcode #884 Uncommon Words from Two Sentences

A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

Example 1:
Input: s1 = "this apple is sweet", s2 = "this apple is sour"
Output: ["sweet","sour"]

Example 2:
Input: s1 = "apple apple", s2 = "banana"
Output: ["banana"]

Constraints:
1 <= s1.length, s2.length <= 200
s1 and s2 consist of lowercase English letters and spaces.
s1 and s2 do not have leading or trailing spaces.
All the words in s1 and s2 are separated by a single space.


Algorithm/DS used: hash map. Mapping words and their occurrences in both sentences

O(N) worst case time where N is the length of s1 + s2

O(N) worst case space where N is the total length of s1 + s2 assuming all words in s1 and s2 are uncommon

"""
from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_and_s2 = s1.split() + s2.split()
        words_dict = {}
        result = []
        for word in s1_and_s2:
            if word in words_dict:
                words_dict[word] += 1
            else:
                words_dict[word] = 1
        for (key, value) in words_dict.items():
            if value == 1:
                result.append(key)
        return result


def test_solution():
    s = Solution()
    print("Expected result from input s1 = \"this apple is sweet\", s2 = \"this apple is sour\" is [\"sweet\",\"sour\"] and the Actual result is: " +
          str(s.uncommonFromSentences("this apple is sweet", "this apple is sour")))
    assert s.uncommonFromSentences(
        "this apple is sweet", "this apple is sour") == ["sweet", "sour"]
    assert s.uncommonFromSentences("s z z z s", "s z ejt") == ["ejt"]


if __name__ == "__main__":
    test_solution()
