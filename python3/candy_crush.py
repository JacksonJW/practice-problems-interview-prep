"""
Leetcode #723 Candy Crush

This question is about implementing a basic elimination algorithm for Candy Crush.

Given an m x n integer array board representing the grid of candy where board[i][j] 
represents the type of candy. A value of board[i][j] == 0 represents that the cell 
is empty.

The given board represents the state of the game following the player's move. Now, 
you need to restore the board to a stable state by crushing candies according to the 
following rules:

If three or more candies of the same type are adjacent vertically or horizontally, 
crush them all at the same time - these positions become empty.
After crushing all candies simultaneously, if an empty space on the board has candies 
on top of itself, then these candies will drop until they hit a candy or bottom at the 
same time. No new candies will drop outside the top boundary.
After the above steps, there may exist more candies that can be crushed. If so, you 
need to repeat the above steps.
If there does not exist more candies that can be crushed (i.e., the board is stable), 
then return the current board.
You need to perform the above rules until the board becomes stable, then return the 
stable board.


Example 1:
Input: board = [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],
[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],
[1,1,2,2,2],[4,1,4,4,1014]]
Output: [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[110,0,0,0,114],[210,0,0,0,214],
[310,0,0,113,314],[410,0,0,213,414],[610,211,112,313,614],[710,311,412,613,714],
[810,411,512,713,1014]]

Example 2:
Input: board = [[1,3,5,5,2],[3,4,3,3,1],[3,2,4,5,2],[2,4,4,5,5],[1,4,4,1,1]]
Output: [[1,3,0,0,0],[3,4,0,5,2],[3,2,0,3,1],[2,4,0,5,2],[1,4,3,1,1]]

Constraints:
m == board.length
n == board[i].length
3 <= m, n <= 50
1 <= board[i][j] <= 2000

Algorithm/DS used: Depth first traversal, hash-table for keeping track of crushed 
locations

O(N^2) worst case time since we can visit certain parts of the board repeatedly

O(N) worst case space where N is the length of the m x n input that could be inserted 
in the table

"""


from collections import deque
from typing import Tuple, List


class Solution:
    def _addToCrushTable(self, crush_list: List[Tuple[int]], crush_table: dict) -> dict:
        if len(crush_list) > 2:
            for i, j in crush_list:
                if j not in crush_table:
                    crush_table[j] = set()
                crush_table[j].add(i)
        return crush_table

    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        is_crushed = False
        while not is_crushed:
            crush_table = {}
            for i in range(len(board)):
                for j, e in enumerate(board[i]):
                    if e != 0:
                        s_right, s_bottom = [], []
                        if j + 1 < len(board[i]):
                            s_right += [(i, j + 1)]
                        if i + 1 < len(board):
                            s_bottom += [(i + 1, j)]
                        crush_list = [(i, j)]
                        while s_right:
                            position = s_right.pop()
                            if board[position[0]][position[1]] == e:
                                crush_list += [position]
                                if position[1] + 1 < len(board[i]):
                                    s_right.append(
                                        (position[0], position[1] + 1))
                        crush_table = self._addToCrushTable(
                            crush_list, crush_table)
                        crush_list = [(i, j)]
                        while s_bottom:
                            position = s_bottom.pop()
                            if board[position[0]][position[1]] == e:
                                crush_list += [position]
                                if position[0] + 1 < len(board):
                                    s_bottom.append(
                                        (position[0] + 1, position[1]))
                        crush_table = self._addToCrushTable(
                            crush_list, crush_table)
            if len(crush_table) == 0:
                is_crushed = True
            elif len(crush_table) > 0:
                for j in range(len(board[0])):
                    if j in crush_table:
                        num_zeros = len(crush_table[j])
                        candy_list = deque()
                        i = 0
                        while i < len(board) and (num_zeros > 0 or len(candy_list) > 0):
                            if i not in crush_table[j]:
                                candy_list.append(board[i][j])
                            if num_zeros > 0:
                                board[i][j] = 0
                                num_zeros -= 1
                            elif len(candy_list) > 0:
                                board[i][j] = candy_list.popleft()
                            i += 1
        return board


def test_solution():
    s = Solution()
    print("Expected result from input [[110,5,112,113,114],[210,211,5,213,214],\
     [310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],\
         [710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]] is \
         [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[110,0,0,0,114],[210,0,0,0,214],\
             [310,0,0,113,314],[410,0,0,213,414],[610,211,112,313,614],\
                 [710,311,412,613,714],[810,411,512,713,1014]] and the Actual \
                     result is: " +
          str(s.candyCrush([[110, 5, 112, 113, 114], [210, 211, 5, 213, 214],
                            [310, 311, 3, 313, 314], [
                                410, 411, 412, 5, 414], [5, 1, 512, 3, 3],
                            [610, 4, 1, 613, 614], [
                                710, 1, 2, 713, 714], [810, 1, 2, 1, 1],
                            [1, 1, 2, 2, 2], [4, 1, 4, 4, 1014]])))
    assert s.candyCrush([[110, 5, 112, 113, 114], [210, 211, 5, 213, 214],
                         [310, 311, 3, 313, 314], [
        410, 411, 412, 5, 414], [5, 1, 512, 3, 3],
        [610, 4, 1, 613, 614], [
        710, 1, 2, 713, 714], [810, 1, 2, 1, 1],
        [1, 1, 2, 2, 2], [4, 1, 4, 4, 1014]]) == [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
                                                  [0, 0, 0, 0, 0], [110, 0, 0, 0, 114], [
                                                      210, 0, 0, 0, 214],
                                                  [310, 0, 0, 113, 314], [410, 0, 0, 213, 414], [
                                                      610, 211, 112, 313, 614],
                                                  [710, 311, 412, 613, 714],
                                                  [810, 411, 512, 713, 1014]]


if __name__ == "__main__":
    test_solution()
