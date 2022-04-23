"""
Leetcode #204 Count Primes

Given an integer n, return the number of prime numbers that are
strictly less than n.

Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 
2, 3, 5, 7.

Example 2:
Input: n = 0
Output: 0

Example 3:
Input: n = 1
Output: 0
 
Constraints:
0 <= n <= 5 * 106

Algorithm/DS used: sieving future composite numbers given a prime #

O(N) worst case time where N is all numbers less than input n

O(N) worst case space where N is input n

"""


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        count = 0
        is_prime = [False, False] + [True]*(n-2)
        for i in range(2, len(is_prime)):
            if is_prime[i]:
                count += 1
                for j in range(i * 2, len(is_prime), i):
                    is_prime[j] = False
        return count


def test_solution():
    s = Solution()
    print("Expected result from input 10 is 4 and the Actual result is: " +
          str(s.countPrimes(10)))
    assert s.countPrimes(10) == 4
    assert s.countPrimes(0) == 0
    assert s.countPrimes(1) == 0
    assert s.countPrimes(100000) == 9592


if __name__ == "__main__":
    test_solution()
