"""
Leetcode #1022 Sum of Root To Leaf Binary Numbers

Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path_str represents a binary number starting with the most significant bit.  For example, if the path_str is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path_str from the root to that leaf.

Return the sum of these numbers.

 

Example 1:



Input: [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
 

Note:

The number of nodes in the tree is between 1 and 1000.
node.val is 0 or 1.
The answer will not exceed 2^31 - 1.

Algorithm/DS used: <ALGORITHM USED/DS USED>

O(n) worst case time

O(n) worst case space

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.paths = []

    def sumRootToLeaf(self, root: TreeNode) -> int:
        result_sum = 0
        self._traverse_paths(root, "")
        for path_str in self.paths:
            result_sum += self._convert_binary_str_to_int(path_str)
        return result_sum

    def _traverse_paths(self, node, path_str):
        if node is None:
            return
        path_str += str(node.val)
        if not node.left and not node.right:
            self.paths.append(path_str)
        self._traverse_paths(node.left, path_str)
        self._traverse_paths(node.right, path_str)

    def _convert_binary_str_to_int(self, binary_str):
        result_int = 0
        for i in range(len(binary_str)):
            if binary_str[i] == "0":
                result_int *= 2
            else:
                result_int = (result_int*2)+1
        return result_int


def test_solution():
    s = Solution()
    t = TreeNode(1)
    t.left = TreeNode(0)
    t.right = TreeNode(1)
    t.left.left = TreeNode(0)
    t.left.right = TreeNode(1)
    t.right.left = TreeNode(0)
    t.right.right = TreeNode(1)
    print("Expected result is 22 and the Actual result is: " +
          str(s.sumRootToLeaf(t)))


if __name__ == "__main__":
    test_solution()
