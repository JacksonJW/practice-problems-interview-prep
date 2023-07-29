"""
Leetcode #1342 Number of Steps to Reduce a Number to Zero

Given a non-negative integer num, return the number of steps to 
reduce it to zero. If the current number is even, you have to 
divide it by 2, otherwise, you have to subtract 1 from it.


Example 1:
Input: num = 14
Output: 6
Explanation: 
    Step 1) 14 is even; divide by 2 and obtain 7. 
    Step 2) 7 is odd; subtract 1 and obtain 6.
    Step 3) 6 is even; divide by 2 and obtain 3. 
    Step 4) 3 is odd; subtract 1 and obtain 2. 
    Step 5) 2 is even; divide by 2 and obtain 1. 
    Step 6) 1 is odd; subtract 1 and obtain 0.



Example 2:
Input: num = 8
Output: 4
Explanation: 
    Step 1) 8 is even; divide by 2 and obtain 4. 
    Step 2) 4 is even; divide by 2 and obtain 2. 
    Step 3) 2 is even; divide by 2 and obtain 1. 
    Step 4) 1 is odd; subtract 1 and obtain 0.



Example 3:
Input: num = 123
Output: 12
 

Constraints:

0 <= num <= 10^6

Algorithm/DS used: Number rules

O(log(num)) worst case time where num is the value of the input

O(log(num)) worst case space where num is the value of the input

"""


class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num <= 0:
            return 0
        num_steps = 0
        while num > 0:
            if num % 2 == 1:
                num -= 1
                num_steps += 1
            else:
                num = num / 2
                num_steps += 1
        return num_steps


def test_solution():
    s = Solution()
    print("Expected result from input 14 is 6 and the Actual result is: " +
          str(s.numberOfSteps(14)))
    assert s.numberOfSteps(14) == 6


if __name__ == "__main__":
    test_solution()
