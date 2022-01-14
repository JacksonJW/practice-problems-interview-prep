"""
Leetcode #144 Binary Tree Preorder Traversal

Given the root of a binary tree, return the preorder
traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,2,3]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]
 
Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100


Algorithm/DS used: Linear preorder traversal DFS using stack

O(N) worst case time where N is the number of nodes in the tree

O(M) worst case space where M is the number of nodes for the 
height of the binary tree nodes

"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        stack.append(root)
        result = []
        while True:
            current_node = stack.pop()
            if current_node:
                result.append(current_node.val)
                stack.append(current_node.right)
                stack.append(current_node.left)
            elif not stack:
                break
        return result


def test_solution():
    n = TreeNode(1, None, TreeNode(2, TreeNode(3, None, None), None))
    n2 = None
    n3 = TreeNode(1, None, None)
    s = Solution()
    print(
        "Expected result from input root = [1,null,2,3] is [1,2,3] and the Actual result is: "
        + str(s.preorderTraversal(n))
    )
    assert s.preorderTraversal(n) == [1, 2, 3]
    assert s.preorderTraversal(n2) == []
    assert s.preorderTraversal(n3) == [1]


if __name__ == "__main__":
    test_solution()
