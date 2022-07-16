"""
Leetcode #937 Reorder Data in Log Files

You are given an array of logs. Each log is a space-delimited string of words,
where the first word is the identifier.

There are two types of logs:

Letter-logs: All words (except the identifier) consist of lowercase English 
letters.

Digit-logs: All words (except the identifier) consist of digits.

Reorder these logs so that:
The letter-logs come before all digit-logs.
The letter-logs are sorted lexicographically by their contents. If their contents 
are the same, then sort them lexicographically by their identifiers.
The digit-logs maintain their relative ordering.
Return the final order of the logs.


Example 1:
Input: logs = 
["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: 
["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

Explanation:
The letter-log contents are all different, so their ordering is 
"art can", "art zero", "own kit dig".
The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".

Example 2:
Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]

Constraints:
1 <= logs.length <= 100
3 <= logs[i].length <= 100
All the tokens of logs[i] are separated by a single space.
logs[i] is guaranteed to have an identifier and at least one word after the identifier.

Algorithm(s)/DS used: 
    - Sorting letter list lexicographically by content
    - Merging lists

O(n*log(n)) worst case time where n is the length of logs

O(n) worst case space where n is the length of logs

"""
from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_list, letter_list = [], []
        for log in logs:
            content_sample = log.split()[1]
            if content_sample.isalpha():
                letter_list.append(log)
            elif content_sample.isnumeric():
                digit_list.append(log)
        letter_list = sorted(letter_list, key=lambda x: [
                             x.split()[1:]] + [x.split()[0]])
        return letter_list + digit_list


def test_solution():
    s = Solution()
    print("Expected result from input [\"dig1 8 1 5 1\",\"let1 art can\",\
    \"dig2 3 6\",\"let2 own kit dig\",\"let3 art zero\"] is [\"let1 art can\",\
    \"let3 art zero\",\"let2 own kit dig\",\"dig1 8 1 5 1\",\"dig2 3 6\"] and \
    the Actual result is: " +
          str(s.reorderLogFiles(["dig1 8 1 5 1", "let1 art can", "dig2 3 6",
                                 "let2 own kit dig", "let3 art zero"])))
    assert s.reorderLogFiles(["dig1 8 1 5 1", "let1 art can", "dig2 3 6",
                              "let2 own kit dig", "let3 art zero"]) == \
        ["let1 art can", "let3 art zero",
            "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]
    assert s.reorderLogFiles(["a1 9 2 3 1", "g1 act car", "zo4 4 7",
                              "ab1 off key dog", "a8 act zoo"]) == \
        ["g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"]


if __name__ == "__main__":
    test_solution()
