"""
Leetcode #88 Binary Gap

Given a positive integer N, find and return the longest distance 
between two consecutive 1's in the binary representation of N.

If there aren't two consecutive 1's, return 0.

 

Example 1:
Input: 22
Output: 2
Explanation: 
22 in binary is 0b10110.
In the binary representation of 22, there are three ones, and two consecutive pairs of 1's.
The first consecutive pair of 1's have distance 2.
The second consecutive pair of 1's have distance 1.
The answer is the largest of these two distances, which is 2.


Example 2:
Input: 5
Output: 2
Explanation: 
5 in binary is 0b101.


Example 3:
Input: 6
Output: 1
Explanation: 
6 in binary is 0b110.


Example 4:
Input: 8
Output: 0
Explanation: 
8 in binary is 0b1000.
There aren't any consecutive pairs of 1's in the binary representation of 8, so we return 0.
 

Note:

1 <= N <= 10^9

Algorithm/DS used: O()

O(n) worst case time where n is the length of the binary representation of N - input

O(1) worst case space

"""


class Solution:
    def binaryGap(self, N: int) -> int:
        result = 0
        s = "{0:32b}".format(N)
        previous_one = False
        count = 0

        for c in s:
            if previous_one and c == "1":
                count += 1
                result = max(result, count)
                count = 0
            elif c == "1":
                previous_one = True
            elif previous_one:
                count += 1

        return result


def test_solution():
    s = Solution()
    print("Expected result from input 22 is 2 and the Actual result is: " +
          str(s.binaryGap(22)))
    assert s.binaryGap(22) == 2


if __name__ == "__main__":
    test_solution()
