"""
Leetcode #1854 Maximum Population Year

You are given a 2D integer array logs where each logs[i] = [birthi, deathi]
indicates the birth and death years of the ith person.

The population of some year x is the number of people alive during that year.
The ith person is counted in year x's population if x is in the inclusive
range [birthi, deathi - 1]. Note that the person is not counted in the year
that they die.

Return the earliest year with the maximum population.

Example 1:
Input: logs = [[1993,1999],[2000,2010]]
Output: 1993
Explanation: The maximum population is 1, and 1993 is the earliest year with
this population.

Example 2:
Input: logs = [[1950,1961],[1960,1971],[1970,1981]]
Output: 1960
Explanation:
The maximum population is 2, and it had happened in years 1960 and 1970.
The earlier year between them is 1960.

Constraints:
1 <= logs.length <= 100
1950 <= birthi < deathi <= 2050

Algorithm/DS used: hash map/counter to count the number of year occurrences

O(n*log(n)) worst case time where n is the total number of years specified in logs

O(n) worst case space where n is the number of years specified in logs 

"""


import collections
from typing import List


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        year_count = collections.Counter()
        logs.sort(key=lambda log: log[0])
        for person in logs:
            birth = person[0]
            death_minus_1 = person[1]
            for year in range(birth, death_minus_1):
                year_count[year] += 1
        return year_count.most_common(1)[0][0]


def test_solution():
    s = Solution()
    print("Expected result from input [[1993,1999],[2000,2010]] is 1993 and the Actual result is: " +
          str(s.maximumPopulation([[1993, 1999], [2000, 2010]])))
    assert s.maximumPopulation(
        [[1993, 1999], [2000, 2010]]) == 1993
    assert s.maximumPopulation(
        [[1950, 1961], [1960, 1971], [1970, 1981]]) == 1960
    assert s.maximumPopulation(
        [[2008, 2026], [2004, 2008], [2034, 2035], [1999, 2050], [
            2049, 2050], [2011, 2035], [1966, 2033], [2044, 2049]]) == 2011


if __name__ == "__main__":
    test_solution()
