"""
Leetcode #728 Self Dividing Numbers

A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
Note:

The boundaries of each input argument are 1 <= left <= right <= 10000.

Algorithm/DS used: string iteration 

O(N x M) worst case time where N is the length that exists between 'left' and 'right' and M is the average length of digits of numbers between 'left' and 'right'

O(N) worst case space

"""

from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []

        for i in range(left, right + 1):
            i_as_string = str(i)

            for j in range(0, len(i_as_string)):
                if int(i_as_string[j]) == 0 or i % int(i_as_string[j]) != 0:
                    break
                elif j == len(i_as_string) - 1:
                    result.append(i)

        return result


def test_solution():
    s = Solution()
    print("Expected result from input left = 1, right = 22 is [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22] and the Actual result is: " +
          str(s.selfDividingNumbers(1, 22)))
    assert s.selfDividingNumbers(
        1, 22) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]


if __name__ == "__main__":
    test_solution()
