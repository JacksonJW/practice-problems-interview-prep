"""
Leetcode #56. Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Algorithm/DS used: Two pointers logic appending list

O(n*log(n)) worst case time where n is the length of the input 'intervals'

O(n) worst case space where n is the length of the input 'intervals'

"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        result = []
        i = 0
        intervals.sort(key=lambda s: s[0])
        while i < len(intervals):
            current_merge = intervals[i]
            j = i + 1
            while j < len(intervals):
                if intervals[j][0] <= current_merge[1]:
                    new_tail_value = max(intervals[j][1], current_merge[1])
                    current_merge = [current_merge[0], new_tail_value]
                    j += 1
                else:
                    break
            result.append(current_merge)
            i = j
        return result


def test_solution():
    s = Solution()
    print("Expected result from input [[1,3], [2,6], [8,10], [15,18]] is [[1,6], [8,10], [15,18]] and the Actual result is: " +
          str(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]])))
    assert s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [
        [1, 6], [8, 10], [15, 18]]


if __name__ == "__main__":
    test_solution()
