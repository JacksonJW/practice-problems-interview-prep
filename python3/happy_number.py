"""
Leetcode #202 Happy Number

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: 
Starting with any positive integer, replace the number by the 
sum of the squares of its digits, and repeat the process until 
the number equals 1 (where it will stay), or it loops endlessly 
in a cycle which does not include 1. Those numbers for which 
this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Algorithm/DS used: Cycle detection - hash set.

O(m*n) worst case time where n is the max number of digits of 'n' and 'm' is the number of computations until a cycle is detected.

O(m) worst case space where 'm' is the number of computations until a cycle is detected.

"""


class Solution:
    def isHappy(self, n: int) -> bool:
        if n < 0:
            return False
        if n == 1:
            return True
        seen = set()
        while n != 1:
            n = sum([int(c)**2 for c in str(n)])
            if n in seen:
                return False
            else:
                seen.add(n)
        return True


def test_solution():
    s = Solution()
    print("Expected result from input 19 is True and the Actual result is: " +
          str(s.isHappy(19)))
    assert s.isHappy(19) == True


if __name__ == "__main__":
    test_solution()
