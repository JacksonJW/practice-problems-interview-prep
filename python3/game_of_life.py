"""
Leetcode #289. Game of Life

According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input:
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output:
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time:
You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is
infinite, which would cause problems when the active area encroaches the border of the array.
How would you address these problems?

Algorithm/DS used: 2d array overwrite to conserve space and prevent reallocating an array

O(m*n) worst case time where m is the length of the row and n is the length of the column of the 2d array input

O(m*n) worst case space where m is the length of the row and n is the length of the column of the 2d array input

"""
from typing import List, NamedTuple
import collections


class Solution:
    def __init__(self):
        self.board = None

    def gameOfLife(self, board: List[List[int]]) -> None:
        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j] = [board[i][j], None]

        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j][1] = self.findNextState(board, i, j)

        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j] = board[i][j][1]

        self.board = board

    def findNextState(self, board: List[List[NamedTuple]], i: int, j: int) -> int:
        def count_current_surrounding_1s(board: List[List[NamedTuple]], i: int, j: int) -> int:
            result = 0
            if i - 1 >= 0:
                result += board[i-1][j][0]
                if j - 1 >= 0:
                    result += board[i-1][j-1][0]
                if j + 1 < len(board[i-1]):
                    result += board[i-1][j+1][0]
            if i + 1 < len(board):
                result += board[i+1][j][0]
                if j - 1 >= 0:
                    result += board[i+1][j-1][0]
                if j + 1 < len(board[i+1]):
                    result += board[i+1][j+1][0]
            if j - 1 >= 0:
                result += board[i][j-1][0]
            if j + 1 < len(board[i]):
                result += board[i][j + 1][0]
            return result

        num_1s_surrounding = count_current_surrounding_1s(board, i, j)

        if board[i][j][0] == 1:
            return 0 if num_1s_surrounding < 2 or num_1s_surrounding > 3 else 1
        else:
            return 1 if num_1s_surrounding == 3 else 0


def test_solution():
    s = Solution()
    life_board = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ]
    s.gameOfLife(life_board)
    print("Expected result from input [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]] is [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]] and the Actual result is: " +
          str(s.board))
    assert s.board == [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]


if __name__ == "__main__":
    test_solution()
