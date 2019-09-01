"""
Leetcode #54 Spiral Matrix

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Simulation/hash map

O(m * n) worst case time where n is the number of rows and m is the number of columns

O(m * n) worst case space where n is the number of rows and m is the number of columns stored in 'visited_indices' and 'result' 
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        m, n = len(matrix[0]), len(matrix)
        visited_indices = set()
        traversal_order = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = []
        i, j, curr_direction = 0, 0, 0

        for _ in range(m * n):
            next_pos = (
                i + traversal_order[curr_direction][0], j + traversal_order[curr_direction][1])
            visited_indices.add((i, j))
            result.append(matrix[i][j])
            if next_pos in visited_indices or next_pos[0] == n or next_pos[0] == n or next_pos[1] == m or next_pos[0] < 0 or next_pos[1] < 0:
                curr_direction = (curr_direction+1) % 4

            i += traversal_order[curr_direction][0]
            j += traversal_order[curr_direction][1]
        return result


def main():
    s = Solution()
    print("Expected result is [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7] and the Actual result is: " +
          str(s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])))


if __name__ == "__main__":
    main()
