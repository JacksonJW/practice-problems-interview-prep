"""
Leetcode #258. Add Digits

Given an integer num, repeatedly add all its digits until 
the result has only one digit, and return it.

Example 1:
Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.

Example 2:
Input: num = 0
Output: 0

Constraints:
0 <= num <= 231 - 1

Algorithm/DS used: Iteration and base condition

O(N) worst case time where N is the lenth of digits nums

O(N) worst case space where N is the length of digits nums

"""


class Solution:
    def addDigits(self, num: int) -> int:
        result = str(num)
        while len(result) != 1:
            new_result = 0
            for i in range(len(result)):
                new_result += int(result[i])
            result = str(new_result)
        return int(result)


def test_solution():
    s = Solution()
    print("Expected result from input 38 is 2 and the Actual result is: " +
          str(s.addDigits(38)))
    assert s.your_method_name(38) == 2
    assert s.your_method_name(0) == 0


if __name__ == "__main__":
    test_solution()
