"""
Leetcode #1281 Subtract the Product and Sum of Digits of an Integer

Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 
Example 1:

Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15

Example 2:
Input: n = 4421
Output: 21
Explanation: 
Product of digits = 4 * 4 * 2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21
 
Constraints:
1 <= n <= 10^5

Algorithm/DS used: Iteration and conversion str to int and int to str

O(N) worst case time where N is the length in digits of number n (int)

O(2) worst case space where 2 is the number of variables stored in memory

"""


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product_of_n = 1
        sum_of_n = 0
        for character in str(n):
            product_of_n *= int(character)
            sum_of_n += int(character)
        return product_of_n - sum_of_n


def test_solution():
    s = Solution()
    print("Expected result from input 234 is 15 and the Actual result is: " +
          str(s.subtractProductAndSum(234)))
    assert s.subtractProductAndSum(234) == 15
    assert s.subtractProductAndSum(4421) == 21


if __name__ == "__main__":
    test_solution()
