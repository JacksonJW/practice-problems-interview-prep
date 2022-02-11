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

O(N*M) worst case time where N is the length of strs and M is the min length of each str in strs

O(P) worst case space where P is the length of the longestCOmmonPrefix

"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        result = ""
        min_length = float('inf')
        for s in strs:
            if len(s) < min_length:
                min_length = len(s)
        model = strs[0]
        for j in range(min_length):
            for i in range(1, len(strs)):
                if strs[i][j] != model[j]:
                    return result
            result = result + model[j]
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
