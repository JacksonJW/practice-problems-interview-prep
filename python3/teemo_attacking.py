from typing import List
"""
Leetcode #495. Teemo Attacking

In LOL world, there is a hero called Teemo and his attacking can make his enemy Ashe be in poisoned condition. Now, given the Teemo's attacking ascending time series towards Ashe and the poisoning time duration per Teemo's attacking, you need to output the total time that Ashe is in poisoned condition.

You may assume that Teemo attacks at the very beginning of a specific time point, and makes Ashe be in poisoned condition immediately.

Example 1:
Input: [1,4], 2
Output: 4
Explanation: At time point 1, Teemo starts attacking Ashe and makes Ashe be poisoned immediately. 
This poisoned status will last 2 seconds until the end of time point 2. 
And at time point 4, Teemo attacks Ashe again, and causes Ashe to be in poisoned status for another 2 seconds. 
So you finally need to output 4.
 
Example 2:
Input: [1,2], 2
Output: 3
Explanation: At time point 1, Teemo starts attacking Ashe and makes Ashe be poisoned. 
This poisoned status will last 2 seconds until the end of time point 2. 
However, at the beginning of time point 2, Teemo attacks Ashe again who is already in poisoned status. 
Since the poisoned status won't add up together, though the second poisoning attack will still work at time point 2, it will stop at the end of time point 3. 
So you finally need to output 3.
 

Note:

You may assume the length of given time series array won't exceed 10000.
You may assume the numbers in the Teemo's attacking time series and his poisoning time duration per attacking are non-negative integers, which won't exceed 10,000,000.
 

Algorithm/DS used: Merge Intervals

O(n) worst case time where n is the lenth of input 'timeSeries'

O(1) worst case space

"""


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total_time_poisoned = 0
        for i in range(len(timeSeries)):
            initial_poison_pt = timeSeries[i]
            expected_poison_end = timeSeries[i] + duration
            if i != len(timeSeries)-1:
                next_poision_pt = timeSeries[i+1]
            if i != len(timeSeries)-1 and next_poision_pt < expected_poison_end:
                total_time_poisoned += next_poision_pt-initial_poison_pt
            else:
                total_time_poisoned += duration
        return total_time_poisoned


def test_solution():
    s = Solution()
    print("Expected result from input [1, 2, 3, 7, 10], 3 is 11 and the Actual result is: " +
          str(s.findPoisonedDuration([1, 2, 3, 7, 10], 3)))
    assert s.findPoisonedDuration([1, 2, 3, 7, 10], 3) == 11


if __name__ == "__main__":
    test_solution()
