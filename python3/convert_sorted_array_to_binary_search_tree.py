"""
Leetcode #108 Convert Sorted Array to Binary Search Tree

Given an integer array nums where the elements are 
sorted in ascending order, convert it to a height-balanced 
binary search tree.

A height-balanced binary tree is a binary tree in which the 
depth of the two subtrees of every node never differs by 
more than one.

Example 1:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.

Algorithm/DS used: Binary search using midpoint for creating a 
node and stack for traversal

O(N) worst case time where N is the length of nums

O(N) worst case space where N is the length of nums

"""
from typing import List
from typing import Tuple
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _createNodeFromMidpoint(self, nums: List[int]) -> Tuple[TreeNode, List, List]:
        if not nums:
            return (None, [], [])
        m = len(nums) // 2
        return (TreeNode(val=nums[m]), nums[:m], nums[m+1:])

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        m = len(nums) // 2
        root = TreeNode(val=nums[m])
        s = [(root, nums[:m], nums[m+1:])]
        while s:
            current = s.pop()
            left = self._createNodeFromMidpoint(current[1])
            right = self._createNodeFromMidpoint(current[2])
            current[0].left = left[0]
            current[0].right = right[0]
            if left[0]:
                s.append(left)
            if right[0]:
                s.append(right)
        return root


def breadth_first_traverse(root: TreeNode) -> List:
    result = []
    q = deque()
    q.append(root)
    while q:
        current = q.popleft()
        if not current:
            result.append(current)
        elif current:
            result.append(current.val)
            if current.left or current.right:
                q.append(current.left)
                q.append(current.right)
    return result


def test_solution():
    s = Solution()
    print("Expected result from input [-10,-3,0,5,9] is [0,-3,9,-10,None,5, None] and the Actual result is: " +
          str(breadth_first_traverse(s.sortedArrayToBST([-10, -3, 0, 5, 9]))))
    assert breadth_first_traverse(s.sortedArrayToBST(
        [-10, -3, 0, 5, 9])) == [0, -3, 9, -10, None, 5, None]
    assert breadth_first_traverse(s.sortedArrayToBST(
        [1, 3])) == [3, 1, None]

    # Insert more tests here...


if __name__ == "__main__":
    test_solution()
