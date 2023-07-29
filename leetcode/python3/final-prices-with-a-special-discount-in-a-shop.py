"""
Leetcode #1475 Final Prices With a Special Discount in a Shop

Given the array prices where prices[i] is the price of the ith item in a shop. There is a special discount for items in the shop, if you buy the ith item, then you will receive a discount equivalent to prices[j] where j is the minimum index such that j > i and prices[j] <= prices[i], otherwise, you will not receive any discount at all.

Return an array where the ith element is the final price you will pay for the ith item of the shop considering the special discount.

Example 1:
Input: prices = [8,4,6,2,3]
Output: [4,2,4,2,3]
Explanation: 
For item 0 with price[0]=8 you will receive a discount equivalent to prices[1]=4, therefore, the final price you will pay is 8 - 4 = 4. 
For item 1 with price[1]=4 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 4 - 2 = 2. 
For item 2 with price[2]=6 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 6 - 2 = 4. 
For items 3 and 4 you will not receive any discount at all.

Example 2:
Input: prices = [1,2,3,4,5]
Output: [1,2,3,4,5]
Explanation: In this case, for all items, you will not receive any discount at all.

Example 3:
Input: prices = [10,1,1,6]
Output: [9,0,1,6]

Constraints:
1 <= prices.length <= 500
1 <= prices[i] <= 10^3

Algorithm/DS used: double for loop iteration

O(n*log(n)) worst case time where n is the length of prices. The n comes from the outer loop. The log(n) comes from the inner loop.

O(n) worst case space where n is the length of prices

"""
from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = []
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    result.append(prices[i] - prices[j])
                    break
                elif j == len(prices) - 1:
                    result.append(prices[i])
            if i == len(prices) - 1:
                result.append(prices[i])
        return result


def test_solution():
    s = Solution()
    print("Expected result from input [8, 4, 6, 2, 3] is [4, 2, 4, 2, 3] and the Actual result is: " +
          str(s.finalPrices([8, 4, 6, 2, 3])))
    assert s.finalPrices([8, 4, 6, 2, 3]) == [4, 2, 4, 2, 3]
    assert s.finalPrices([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert s.finalPrices([10, 1, 1, 6]) == [9, 0, 1, 6]


if __name__ == "__main__":
    test_solution()
