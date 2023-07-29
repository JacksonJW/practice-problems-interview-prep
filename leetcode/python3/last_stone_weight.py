"""
Leetcode #1046 Last Stone Weight

You are given an array of integers stones where stones[i] 
is the weight of the ith stone.

We are playing a game with the stones. On each turn, we 
choose the heaviest two stones and smash them together. 
Suppose the heaviest two stones have weights x and y with 
x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the 
stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the smallest possible weight of the left stone. If 
there are no stones left, return 0.


Example 1:
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then 
that's the value of the last stone.

Example 2:
Input: stones = [1]
Output: 1

Constraints:
1 <= stones.length <= 30
1 <= stones[i] <= 1000

Algorithm/DS used: Iteration and sorting

O(N^2) worst case time where N is the length of the input

O(N) worst case space where N is the length of the input

"""
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        new_stones = stones
        while len(new_stones) > 1:
            new_stones = sorted(new_stones)
            result_stone = new_stones[len(
                new_stones)-1] - new_stones[len(new_stones)-2]
            if result_stone == 0:
                new_stones = new_stones[:len(new_stones)-2]
            else:
                new_stones.pop()
                new_stones[len(new_stones)-1] = result_stone
        return 0 if len(new_stones) == 0 else new_stones[0]


def test_solution():
    s = Solution()
    print("Expected result from input [2,7,4,1,8,1] is 1 and the Actual result is: " +
          str(s.lastStoneWeight([2, 7, 4, 1, 8, 1])))
    assert s.lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1
    assert s.lastStoneWeight([3, 7, 2]) == 2


if __name__ == "__main__":
    test_solution()
