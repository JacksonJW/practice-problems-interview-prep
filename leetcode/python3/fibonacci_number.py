"""
Leetcode #509. Fibonacci Number

The Fibonacci numbers, commonly denoted F(n) form a sequence,
called the Fibonacci sequence, such that each number is the
sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).

Example 1:
Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:
Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:
Input: 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.


Note:
0 ≤ N ≤ 30.

Algorithm/DS used: <ALGORITHM USED/DS USED>

O(N) worst case time where N is the number specified in the the input

O(N) worst case space where N is the number specified in the the input

"""


class Solution:
    def fib(self, N: int) -> int:
        fib_lookup = [0, 1]
        n = 0
        sum = 0
        while n <= N:
            sum = 0
            if n < len(fib_lookup):
                sum += fib_lookup[n]
            else:
                sum += fib_lookup[n-1] + fib_lookup[n-2]
                fib_lookup.append(sum)
            n += 1
        return sum


def test_solution():
    s = Solution()
    print("Expected result from input 4 is 3 and the Actual result is: " +
          str(s.fib(4)))
    assert s.fib(4) == 3


if __name__ == "__main__":
    test_solution()
