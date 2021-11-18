"""
Leetcode #234. Palindrome Linked List

Given the head of a singly linked list, return true 
if it is a palindrome.
 
Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
 

Constraints:
The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9

Algorithm/DS used: Iteration. Store node values in list

O(N) worst case time where N is the length of the linked list

O(N) worst case space where N is the length of the linked list

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        pointer = head
        l = []
        while pointer is not None:
            l.append(pointer.val)
            pointer = pointer.next
        for i, v in enumerate(l[:len(l)//2]):
            if v != l[len(l)-1-i]:
                return False
        return True


def test_solution():
    s = Solution()
    l = ListNode(1, ListNode(2, ListNode(2, ListNode(1, None))))
    l2 = ListNode(1, ListNode(2, None))
    print("Expected result from input [1,2,2,1] is True and the Actual result is: " +
          str(s.isPalindrome(l)))
    assert s.isPalindrome(l) == True
    assert s.isPalindrome(l2) == False


if __name__ == "__main__":
    test_solution()
