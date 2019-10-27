"""
Leetcode #121. Best Time to Buy and Sell Stock

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

Algorithm/DS used: In-place Array manipulation

O(n) best/worst case time where n is the total amount of integers in the input

O(1) worst case space where the input array is being manipulated and the space stays the same

"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        previous_day_price = prices[0]
        prices[0] = 0
        for i in range(1, len(prices)):
            current_day_price = prices[i]
            prices[i] = (current_day_price - previous_day_price) + prices[i-1]
            previous_day_price = current_day_price
        price_to_buy = min(prices)
        day_to_buy = prices.index(price_to_buy)
        prices_to_sell = prices[day_to_buy+1:]

        if prices_to_sell and max(prices_to_sell) > price_to_buy:
            return max(prices_to_sell) - price_to_buy

        return 0


def test_solution():
    s = Solution()
    print("Expected result from input [7,1,5,3,6,4] is 5 and the Actual result is: " +
          str(s.maxProfit([7, 1, 5, 3, 6, 4])))
    assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 5

    print("Expected result from input [7,6,4,3,1] is 0 and the Actual result is: " +
          str(s.maxProfit([7, 6, 4, 3, 1])))
    assert s.maxProfit([7, 6, 4, 3, 1]) == 0


if __name__ == "__main__":
    test_solution()
