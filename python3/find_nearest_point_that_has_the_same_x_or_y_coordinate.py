"""
Leetcode #1779 Find Nearest Point That Has the Same X or Y Coordinate

You are given two integers, x and y, which represent your current
location on a Cartesian grid: (x, y). You are also given an array
points where each points[i] = [ai, bi] represents that a point exists
at (ai, bi). A point is valid if it shares the same x-coordinate or
the same y-coordinate as your location.

Return the index (0-indexed) of the valid point with the smallest
Manhattan distance from your current location. If there are multiple,
return the valid point with the smallest index. If there are no valid
points, return -1.

The Manhattan distance between two points (x1, y1) and (x2, y2) is
abs(x1 - x2) + abs(y1 - y2).

Example 1:
Input: x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
Output: 2
Explanation: Of all the points, only [3,1], [2,4] and [4,4] are valid. Of the valid points, [2,4] and [4,4] have the smallest Manhattan distance from your current location, with a distance of 1. [2,4] has the smallest index, so return 2.

Example 2:
Input: x = 3, y = 4, points = [[3,4]]
Output: 0
Explanation: The answer is allowed to be on the same location as your current location.

Example 3:
Input: x = 3, y = 4, points = [[2,3]]
Output: -1
Explanation: There are no valid points.

Constraints:
1 <= points.length <= 104
points[i].length == 2
1 <= x, y, ai, bi <= 104
Algorithm/DS used: <ALGORITHM USED/DS USED>

O(N) worst case time where N is the length of points

O(1) worst case space

"""
from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        result = -1
        nearest_distance = float('inf')
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                d = abs(x - points[i][0]) + abs(y - points[i][1])
                if d < nearest_distance:
                    nearest_distance = d
                    result = i
        return result


def test_solution():
    s = Solution()
    print(
        "Expected result from input x = 3, y = 4 [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]] is 2 and the actual result is " + str(s.nearestValidPoint(3, 4, [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]])))
    assert s.nearestValidPoint(
        3, 4, [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]) == 2
    assert s.nearestValidPoint(3, 4, [[3, 4]]) == 0
    assert s.nearestValidPoint(3, 4, [[2, 3]]) == -1
    assert s.nearestValidPoint(1, 1, [[1, 1], [1, 1]]) == 0


if __name__ == "__main__":
    test_solution()
