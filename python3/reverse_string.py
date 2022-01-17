"""
Leetcode #344 Reverse String

Write a function that reverses a string. The input string is 
given as an array of characters s.

You must do this by modifying the input array in-place with 
O(1) extra memory.


Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Constraints:
1 <= s.length <= 105
s[i] is a printable ascii character.

Algorithm/DS used: Using knowledge of language 

O(N) worst case time where N is the length of the s

O(1) worst case space since modifying array in place.

"""
from typing import List


class Solution:
    def reverse_string(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()


def test_solution():
    s = Solution()
    print("Expected result from input [\"h\", \"e\", \"l\", \"l\", \"o\"] is  and the Actual result is: " +
          str(s.reverse_string(["h", "e", "l", "l", "o"])))

    s1 = ["h", "e", "l", "l", "o"]
    assert s.reverse_string(s1) == ["o", "l", "l", "e", "h"]

    s2 = ["H", "a", "n", "n", "a", "h"]
    assert s.reverse_string(s2) == ["h", "a", "n", "n", "a", "H"]


if __name__ == "__main__":
    test_solution()
