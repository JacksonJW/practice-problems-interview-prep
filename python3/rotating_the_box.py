"""
Leetcode #1861 Rotating the Box

You are given an m x n matrix of characters box representing a 
side-view of a box. Each cell of the box is one of the following:

A stone '#'
A stationary obstacle '*'
Empty '.'
The box is rotated 90 degrees clockwise, causing some of the 
stones to fall due to gravity. Each stone falls down until it 
lands on an obstacle, another stone, or the bottom of the box. 
Gravity does not affect the obstacles' positions, and the inertia 
from the box's rotation does not affect the stones' horizontal 
positions.

It is guaranteed that each stone in box rests on an obstacle, 
another stone, or the bottom of the box.

Return an n x m matrix representing the box after the rotation 
described above.


Example 1:
Input: box = [["#",".","#"]]
Output: [["."],
         ["#"],
         ["#"]]

Example 2:
Input: box = [["#",".","*","."],
              ["#","#","*","."]]
Output: [["#","."],
         ["#","#"],
         ["*","*"],
         [".","."]]

Example 3:
Input: box = [["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]]
Output: [[".","#","#"],
         [".","#","#"],
         ["#","#","*"],
         ["#","*","."],
         ["#",".","*"],
         ["#",".","."]]
 

Constraints:
m == box.length
n == box[i].length
1 <= m, n <= 500
box[i][j] is either '#', '*', or '.'.

Algorithm/DS used: Count and overwrite squares

O(N) worst case time where N is the length of the input list 

O(N) worst case space where N is the length of the input list 

"""
from typing import List


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for i in range(len(box)):
            j = 0
            while j < len(box[i]):
                rock_num, space_num, start_j = 0, 0, j
                while j < len(box[i]) and box[i][j] != '*':
                    if box[i][j] == '.':
                        space_num += 1
                    elif box[i][j] == '#':
                        rock_num += 1
                    j += 1

                for temp_j in range(start_j, j):
                    if space_num > 0:
                        box[i][temp_j] = '.'
                        space_num -= 1
                    elif rock_num > 0:
                        box[i][temp_j] = '#'
                        rock_num -= 1

                if j < len(box[i]) and box[i][j] == '*':
                    j += 1

        new_box = [[]] * len(box[0])
        old_i, old_j = len(box) - 1, 0
        for i in range(len(box[0])):
            for _ in range(len(box)):
                new_box[i] = new_box[i] + [box[old_i][old_j]]
                old_i -= 1
            old_i = len(box) - 1
            old_j += 1

        return new_box


def test_solution():
    s = Solution()
    print("Expected result from input [[\"# \",\".\",\"#\"]] \
    is [[\".\"],[\"#\"],[\"#\"]] and the Actual result is : " +
          str(s.rotateTheBox([["#", ".", "#"]])))
    assert s.rotateTheBox([["#", ".", "#"]]) == [["."], ["#"], ["#"]]
    assert s.rotateTheBox(
        [["#", ".", "*", "."], ["#", "#", "*", "."]]) == [["#", "."],
                                                          ["#", "#"],
                                                          ["*", "*"],
                                                          [".", "."]]
    assert s.rotateTheBox([["#", "#", "*", ".", "*", "."],
                           ["#", "#", "#", "*", ".", "."],
                           ["#", "#", "#", ".", "#", "."]]) == [[".", "#", "#"],
                                                                [".", "#", "#"],
                                                                ["#", "#", "*"],
                                                                ["#", "*", "."],
                                                                ["#", ".", "*"],
                                                                ["#", ".", "."]]


if __name__ == "__main__":
    test_solution()
