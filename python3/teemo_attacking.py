from typing import List
"""
Leetcode #<PROBLEM NUMBER AND TITLE>

<LEETCODE PROBLEM DESCRIPTION>

Algorithm/DS used: <ALGORITHM USED/DS USED>

<AVERAGE TIME COMPLEXITY> worst case time

<AVERAGE SPACE COMPLEXITY> worst case space

"""


"""
Replace class 'Solution' with your Leetcode solution below.
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
