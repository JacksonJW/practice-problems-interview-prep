"""
Leetcode #1417 Reformat The String

Given alphanumeric string s. (Alphanumeric string is a string 
consisting of lowercase English letters and digits).

You have to find a permutation of the string where no letter 
is followed by another letter and no digit is followed by 
another digit. That is, no two adjacent characters have the 
same type.

Return the reformatted string or return an empty string if it 
is impossible to reformat the string.


Example 1:
Input: s = "a0b1c2"
Output: "0a1b2c"
Explanation: No two adjacent characters have the same type in 
"0a1b2c". "a0b1c2", "0a1b2c", "0c2a1b" are also valid 
permutations.

Example 2:
Input: s = "leetcode"
Output: ""
Explanation: "leetcode" has only characters so we cannot separate them by digits.

Example 3:
Input: s = "1229857369"
Output: ""
Explanation: "1229857369" has only digits so we cannot separate them by characters.

Example 4:
Input: s = "covid2019"
Output: "c2o0v1i9d"

Example 5:
Input: s = "ab123"
Output: "1a2b3"
 

Constraints:
1 <= s.length <= 500
s consists of only lowercase English letters and/or digits.

Algorithm/DS used: Interleave string/zip. Iteration

O(N) worst case time where N is the length of s

O(N) worst case space where N is the length of s 

"""


class Solution:
    def reformat(self, s: str) -> str:
        n, c = [], []
        result = ''
        for i in range(len(s)):
            if s[i].isdigit():
                n.append(s[i])
            else:
                c.append(s[i])

        if abs(len(n) - len(c)) > 1:
            return result
        elif len(n) - len(c) == 0:
            for i, j in zip(c, n):
                result = result + i + j
        elif len(n) - len(c) == 1:
            for j, i in zip(n, c):
                result = result + j + i
            result += str(n[-1])
        else:
            for i, j in zip(c, n):
                result = result + i + j
            result += str(c[-1])
        return result


def test_solution():
    s = Solution()
    print("Expected result from input 'a0b1c2' is 'a0b1c2' and the Actual result is: " +
          str(s.reformat('a0b1c2')))
    assert s.reformat('a0b1c2') == 'a0b1c2'
    assert s.reformat('leetcode') == ''
    assert s.reformat('1229857369') == ''
    assert s.reformat('covid2019') == 'c2o0v1i9d'
    assert s.reformat('ab123') == '1a2b3'


if __name__ == "__main__":
    test_solution()
