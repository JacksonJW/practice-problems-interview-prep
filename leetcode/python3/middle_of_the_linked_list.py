"""
Leetcode #876. Middle of the Linked List

Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:

Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
Example 2:

Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Note:

The number of nodes in the given list will be between 1 and 100.

Algorithm/DS used: hash table storing nodes

O(n) worst case time where n is 

O(n) worst case space where n is the size of the hash table

"""


"""
Replace class 'Solution' with your Leetcode solution below.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head):
        current_node = head
        nodes_by_num = {}
        nodes_count = 0
        while current_node is not None:
            nodes_count += 1
            nodes_by_num[nodes_count] = current_node
            current_node = current_node.next
        return nodes_by_num[(nodes_count//2)+1]


def test_solution():
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)
    node.next.next.next.next = ListNode(5)
    s = Solution()
    assert s.middleNode(node).val == 3
    print("Expected result is 3 and the Actual result is: " +
          str(s.middleNode(node).val))


if __name__ == "__main__":
    test_solution()
