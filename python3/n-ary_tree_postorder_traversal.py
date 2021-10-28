"""
Leetcode #590 N-ary Tree Postorder Traversal

Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]

Example 2:
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,
    null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]

Constraints:
The number of nodes in the tree is in the range [0, 104].
0 <= Node.val <= 104
The height of the n-ary tree is less than or equal to 1000.

Follow up: Recursive solution is trivial, could you do it iteratively?

Algorithm/DS used: Iterative postorder traversal w/ stack

O(N) worst case time where N is the number of nodes in the tree

O(N) worst case space where N is the number of nodes in the tree

"""
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        result = []
        stack = [root]
        while len(stack) > 0:
            parent = stack[-1]
            if stack[-1].children:
                for child in reversed(stack[-1].children):
                    stack.append(child)
                parent.children = None
            else:
                result.append(stack.pop().val)
        return result


def test_solution():
    s = Solution()
    print("Expected result from input root = [1,null,3,2,4,null,5,6] is [5,6,3,2,4,1] and the Actual result is: " +
          str(s.postorder([1, None, 3, 2, 4, None, 5, 6])))
    assert s.postorder([1, None, 3, 2, 4, None, 5, 6]) == [5, 6, 3, 2, 4, 1]
    assert s.postorder([1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9,
                        10, None, None, 11, None, 12, None, 13, None, None, 14]) == [2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1]


if __name__ == "__main__":
    test_solution()
