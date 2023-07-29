"""
Leetcode #226 Invert Binary Tree

Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.

Algorithm/DS used: preorder traversal DFS

O(n) worst case time where n is the number of nodes in the binary tree

O(1) worst case space since we are modifying the leaves of the binary tree in place

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        self.swapLeftAndRight(root)
        return root

    def swapLeftAndRight(self, node):
        if node is None:
            return
        node.left, node.right = node.right, node.left
        self.swapLeftAndRight(node.left)
        self.swapLeftAndRight(node.right)

    def traverseFinalTreeBFS(self, root):
        queue = []
        result = []
        current_node = root
        queue.append(current_node)
        while queue:
            current_node = queue.pop(0)
            result.append(current_node.val)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return result


def test_solution():
    node = TreeNode(4)
    node.left = TreeNode(2)
    node.right = TreeNode(7)
    node.left.left = TreeNode(1)
    node.left.right = TreeNode(3)
    node.right.left = TreeNode(6)
    node.right.right = TreeNode(9)
    s = Solution()
    print("Expected result from input [4, 2, 7, 1, 3, 6, 9] is [4, 7, 2, 9, 6, 3, 1] and the Actual result is: " +
          str(s.traverseFinalTreeBFS(s.invertTree(node))))
    assert s.traverseFinalTreeBFS(node) == [4, 7, 2, 9, 6, 3, 1]


if __name__ == "__main__":
    test_solution()
