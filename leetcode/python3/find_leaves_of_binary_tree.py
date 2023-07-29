"""
Leetcode #366 Find Leaves of Binary Tree

Given the root of a binary tree, collect a tree's nodes as if
you were doing this:

Collect all the leaf nodes.
Remove all the leaf nodes.
Repeat until the tree is empty.

Example 1:
Input: root = [1,2,3,4,5]
Output: [[4,5,3],[2],[1]]
Explanation:
[[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered
correct answers since per each level it does not matter the
order on which elements are returned.

Example 2:
Input: root = [1]
Output: [[1]]

Constraints:
The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100

Algorithm/DS used: <ALGORITHM USED/DS USED>

<AVERAGE TIME COMPLEXITY> worst case time

<AVERAGE SPACE COMPLEXITY> worst case space

"""

# Definition for a binary tree node.
from typing import Optional, List
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        output = []
        while root:
            result = []
            q.append((root, '', None))
            while q:
                current_node = q.popleft()
                if current_node[0].right:
                    q.append((current_node[0].right, 'right', current_node[0]))
                if current_node[0].left:
                    q.append((current_node[0].left, 'left', current_node[0]))
                if not current_node[0].left and not current_node[0].right:
                    result.append(current_node[0].val)
                    if current_node[1] == 'left':
                        current_node[2].left = None
                    elif current_node[1] == 'right':
                        current_node[2].right = None
                    else:
                        root = None
            output.append(result)
        return output


def test_solution():
    root = TreeNode(1, TreeNode(2, TreeNode(4, None, None),
                                TreeNode(5, None, None)), TreeNode(3, None, None))
    s = Solution()
    print("Expected result from input [1, 2, 3, 4, 5] is [[3, 5, 4], [2], [1]] and \
        the Actual result is: " + str(s.findLeaves(root)))
    print()
    assert [[3, 5, 4], [2], [1]] == [[3, 5, 4], [2], [1]]
    assert s.findLeaves(root) == [[3, 5, 4], [2], [1]]


if __name__ == "__main__":
    test_solution()
