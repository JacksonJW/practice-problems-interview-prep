"""
Leetcode #14 Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

Algorithm/DS used: Three pointers iteration

O(n) worst case time

O(m) worst case space where m is the length of the longestCOmmonPrefix

"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or not all(strs):
            return ""
        current_index = 0
        result = ""
        smallest_str_len = min([len(s) for s in strs])

        while current_index < smallest_str_len:
            similar_letter = ""
            is_similar = True
            for s in strs:
                if not similar_letter:
                    similar_letter = s[current_index]
                elif s[current_index] != similar_letter:
                    is_similar = False
                    break
            if not is_similar:
                break
            else:
                result += similar_letter
                current_index += 1
        return result


def test_solution():
    s = Solution()
    print("Expected result from input [\"flower\",\"flow\",\"flight\"] is \"fl\" and the Actual result is: " +
          str(s.longestCommonPrefix(["flower", "flow", "flight"])))
    assert s.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"

    print("Expected result from input [\"dog\",\"racecar\",\"car\"] is \"\" and the Actual result is: " +
          str(s.longestCommonPrefix(["dog", "racecar", "car"])))
    assert s.longestCommonPrefix(["dog", "racecar", "car"]) == ""


if __name__ == "__main__":
    test_solution()
