"""
Leetcode #9 Palindrome Number

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

Example 1:

Input: x = 121
Output: true
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Example 4:

Input: x = -101
Output: false

Constraints:

-231 <= x <= 231 - 1

Algorithm/DS used: Loop and compare first and last characters in converted str

O(N) worst case time where N is the number of digits for x due to the str() operator

O(1) worst case space

"""
import math


class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_as_string = str(x)
        for i in range(math.floor(len(num_as_string)/2)):
            if num_as_string[i] != num_as_string[-1 - i]:
                return False
        return True


def test_solution():
    s = Solution()
    print("Expected result from input 121 is True and the Actual result is: " +
          str(s.isPalindrome(121)))
    assert s.isPalindrome(121) == True
    assert s.isPalindrome(-121) == False
    assert s.isPalindrome(10) == False


if __name__ == "__main__":
    test_solution()
