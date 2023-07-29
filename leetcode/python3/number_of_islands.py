"""
Leetcode #200 Number of Islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input:
11110
11010
11000
00000
Output: 1

Example 2:
Input:
11000
11000
00100
00011
Output: 3

Algorithm/DS used: BFS graph traversal and hashmap to hold visited coordinates

O(n) worst case time where n is the length of the 2d array

O(n+q) worst case space where n is the number of coordinates in visited and q is the number of items added to the queue for BFS.

"""
import collections
from typing import List


import collections
from typing import List


class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count = 0
        m = len(grid)
        n = len(grid[0])
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in visited:
                    count += 1
                    visited = self.traverse_island(grid, i, j, visited)
        return count

    def traverse_island(self, grid, i, j, visited):
        q = collections.deque()
        q.append((i, j))
        m = len(grid)
        n = len(grid[0])
        visited.add((i, j))

        while q:
            i_pos, j_pos = q.popleft()

            if 0 <= i_pos-1 and (i_pos-1, j_pos) not in visited and grid[i_pos-1][j_pos] == '1':
                q.append((i_pos-1, j_pos))
                visited.add((i_pos-1, j_pos))
            if j_pos+1 < n and (i_pos, j_pos+1) not in visited and grid[i_pos][j_pos+1] == '1':
                q.append((i_pos, j_pos+1))
                visited.add((i_pos, j_pos+1))
            if i_pos+1 < m and (i_pos+1, j_pos) not in visited and grid[i_pos+1][j_pos] == '1':
                q.append((i_pos+1, j_pos))
                visited.add((i_pos+1, j_pos))
            if 0 <= j_pos-1 and (i_pos, j_pos-1) not in visited and grid[i_pos][j_pos-1] == '1':
                q.append((i_pos, j_pos-1))
                visited.add((i_pos, j_pos-1))

        return visited


def test_solution():
    s = Solution()
    print("Expected result from input [\"11000\", \"11000\", \"00100\", \"00011\"] is 3 and the Actual result is: " +
          str(s.numIslands(["11000", "11000", "00100", "00011"])))
    assert s.numIslands(["11000", "11000", "00100", "00011"]) == 3
    assert s.numIslands(["1111", "1101", "1100", "0000"]) == 1


if __name__ == "__main__":
    test_solution()
