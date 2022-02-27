"""
Leetcode #2034 Stock Price Fluctuation

You are given a stream of records about a particular stock. Each record
contains a timestamp and the corresponding price of the stock at that
timestamp.

Unfortunately due to the volatile nature of the stock market, the records
do not come in order. Even worse, some records may be incorrect. Another
record with the same timestamp may appear later in the stream correcting
the price of the previous wrong record.

Design an algorithm that:
 - Updates the price of the stock at a particular timestamp, correcting the
 - price from any previous records at the timestamp.
 - Finds the latest price of the stock based on the current records. The
 - latest price is the price at the latest timestamp recorded.
 - Finds the maximum price the stock has been based on the current records.
 - Finds the minimum price the stock has been based on the current records.


Implement the StockPrice class:
 - StockPrice() Initializes the object with no price records.
 - void update(int timestamp, int price) Updates the price of the stock at
 - the given timestamp.
 - int current() Returns the latest price of the stock.
 - int maximum() Returns the maximum price of the stock.
 - int minimum() Returns the minimum price of the stock.


Example 1:
Input
["StockPrice", "update", "update", "current",
    "maximum", "update", "maximum", "update", "minimum"]
[[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]
Output
[null, null, null, 5, 10, null, 5, null, 2]

Explanation
StockPrice stockPrice = new StockPrice();
stockPrice.update(1, 10); // Timestamps are [1] with corresponding prices [10].
stockPrice.update(2, 5);  // Timestamps are [1,2] with corresponding prices [10,5].
stockPrice.current();     // return 5, the latest timestamp is 2 with the price being 5.
stockPrice.maximum();     // return 10, the maximum price is 10 at timestamp 1.
stockPrice.update(1, 3);  // The previous timestamp 1 had the wrong price, so it is updated to 3.
                          // Timestamps are [1,2] with corresponding prices [3,5].
stockPrice.maximum();     // return 5, the maximum price is 5 after the correction.
stockPrice.update(4, 2);  // Timestamps are [1,2,4] with corresponding prices [3,5,2].
stockPrice.minimum();     // return 2, the minimum price is 2 at timestamp 4.


Constraints:
1 <= timestamp, price <= 109
At most 105 calls will be made in total to update, current, maximum, and minimum.
current, maximum, and minimum will be called only after update has been called at least once.

Algorithm/DS used: <ALGORITHM USED/DS USED>

O(M) worst case time where M is the length of min_heap or max_heap and there have been multiple updates to the same timestamp

O(N) worst case space where N is the number of updates for new numbers

"""

import heapq


class StockPrice:
    def __init__(self):
        self.prices = {}
        self.max_heap = []
        self.min_heap = []
        self.current_timestamp = float('-inf')

    def update(self, timestamp: int, price: int) -> None:
        if timestamp > self.current_timestamp:
            self.current_timestamp = timestamp
        self.prices[timestamp] = price
        heapq.heappush(self.max_heap, (-price, timestamp))
        heapq.heappush(self.min_heap, (price, timestamp))

    def current(self) -> int:
        return self.prices[self.current_timestamp]

    def maximum(self) -> int:
        while self.max_heap[0][0] * -1 != self.prices[self.max_heap[0][1]]:
            heapq.heappop(self.max_heap)
        return self.max_heap[0][0] * -1

    def minimum(self) -> int:
        while self.min_heap[0][0] != self.prices[self.min_heap[0][1]]:
            heapq.heappop(self.min_heap)
        return self.min_heap[0][0]


def test_solution():
    stockPrice = StockPrice()
    stockPrice.update(1, 10)
    stockPrice.update(2, 5)
    assert stockPrice.current() == 5
    print("Expected result from input stockPrice.current() is 5 and the Actual result is: " +
          str(stockPrice.current()))
    assert stockPrice.maximum() == 10
    stockPrice.update(1, 3)
    assert stockPrice.maximum() == 5
    print("Expected result from input stockPrice.maximum() is 5 and the Actual result is: " +
          str(stockPrice.maximum()))
    stockPrice.update(4, 2)
    assert stockPrice.minimum() == 2
    print("Expected result from input stockPrice.minimum() is 2 and the Actual result is: " +
          str(stockPrice.minimum()))


if __name__ == "__main__":
    test_solution()
