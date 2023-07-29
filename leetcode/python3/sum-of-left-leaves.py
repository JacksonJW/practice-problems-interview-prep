"""
Leetcode #404 Sum of Left Leaves

Given the root of a binary tree, return the sum of all left leaves.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
Example 2:

Input: root = [1]
Output: 0

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-1000 <= Node.val <= 1000

Algorithm/DS used: Modified preorder traversal

O(N) worst case time where N is the number of nodes in the binary tree

O(N) worst case space where N is the number of nodes in the tree

"""

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        sum = 0
        leaf_stack = [root]
        while len(leaf_stack) != 0:
            leaf = leaf_stack.pop()
            if leaf.right:
                leaf_stack.append(leaf.right)
            if leaf.left:
                leaf_stack.append(leaf.left)
                if leaf.left.left is None and leaf.left.right is None:
                    sum += leaf.left.val
        return sum


def test_solution():

    example1_root = TreeNode(3, None, None)
    example1_root.left = TreeNode(9, None, None)
    example1_root.right = TreeNode(20, None, None)
    example1_root.right.left = TreeNode(15, None, None)
    example1_root.right.right = TreeNode(7, None, None)

    s = Solution()
    print("Expected result from input [3, 9, 20, null, null, 15, 7] is 24 and the Actual result is: " +
          str(s.sumOfLeftLeaves(example1_root)))
    assert s.sumOfLeftLeaves(example1_root) == 24


if __name__ == "__main__":
    test_solution()
