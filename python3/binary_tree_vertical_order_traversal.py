"""
Leetcode #314 Binary Tree Vertical Order Traversal

Given the root of a binary tree, return the vertical order traversal of its 
nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to
right.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]

Example 2:
Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]

Example 3:
Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
Output: [[4],[9,5],[3,0,1],[8,2],[7]]
 

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

Algorithm(s)/DS used: queue for breadth-first traversal and hash table for
keeping track of which nodes go to different columns

O(N) worst case time where N is the number of nodes in the tree

O(N) worst case space where N is the number of nodes in the tree who's values 
help populate the hash table

"""
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q, columns = deque(), {}
        q.append((0, root))
        while q:
            current = q.popleft()
            if current[0] not in columns:
                columns[current[0]] = [current[1].val]
            elif current[0] in columns:
                columns.get(current[0]).append(current[1].val)
            if current[1].left:
                q.append((current[0] - 1, current[1].left))
            if current[1].right:
                q.append((current[0] + 1, current[1].right))

        return [x[1] for x in sorted(columns.items())]


def test_solution():
    s = Solution()
    test_1 = TreeNode(3)
    test_1.left = TreeNode(9)
    test_1.right = TreeNode(8)
    test_1.left.left = TreeNode(4)
    test_1.left.right = TreeNode(0)
    test_1.right.left = TreeNode(1)
    test_1.right.right = TreeNode(7)
    print("Expected result from input [3, 9, 8, 4, 0, 1, 7] is \
    [[4], [9], [3,0,1], [8], [7]] and the Actual result is: "
          + str(s.verticalOrder(test_1)))
    assert s.verticalOrder(test_1) == [[4], [9], [3, 0, 1], [8], [7]]

    test_2 = TreeNode(3)
    test_2.left = TreeNode(9)
    test_2.right = TreeNode(8)
    test_2.left.left = TreeNode(4)
    test_2.left.right = TreeNode(0)
    test_2.right.left = TreeNode(1)
    test_2.right.right = TreeNode(7)
    test_2.left.right.right = TreeNode(2)
    test_2.right.left.left = TreeNode(5)

    assert s.verticalOrder(test_2) == [[4], [9, 5], [3, 0, 1], [8, 2], [7]]


if __name__ == "__main__":
    test_solution()
