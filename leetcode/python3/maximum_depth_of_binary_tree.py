"""
Leetcode #104 Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest 
path from the root node down to the farthest leaf node.

Algorithm/DS used: Depth first tree traversal using stack

O(N) worst case time where N is the number of nodes in the tree

O(log(N)) worst case space where N is the number of nodes in the tree

"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        if not root:
            return max_depth
        stack = [(root, 1)]
        while stack:
            c = stack.pop()
            if c[1] > max_depth:
                max_depth = c[1]
            if c[0].right:
                stack.append((c[0].right, c[1] + 1))
            if c[0].left:
                stack.append((c[0].left, c[1] + 1))
        return max_depth


def test_solution():
    node = TreeNode(3)
    node.left = TreeNode(9)
    node.right = TreeNode(20)
    node.right.left = TreeNode(15)
    node.right.right = TreeNode(7)

    node1 = TreeNode(1)
    node1.right = TreeNode(2)

    s = Solution()
    print("Expected result from input [3,9,20,null,null,15,7] is 3 and the Actual result is: " +
          str(s.maxDepth(node)))
    assert s.maxDepth(node) == 3
    assert s.maxDepth(node1) == 2


if __name__ == "__main__":
    test_solution()
