"""
Leetcode #21 Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

Algorithm/DS used: Bottom up dynamic programming, recursion

O(n + m) worst case time where n is the size of the first list node and m is the size of the second list node

O(n+m) worst case STACK space where n is the size of first list node and m is the size of the second list node

"""
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def interleave_sorted(self, list1, list2):
        p1, p2 = list1, list2
        while p1 is not None and p2 is not None:
            if p1.next is None or p2.val <= p1.next.val:
                new_p1 = p1.next
                p1.next = p2
                p1 = new_p1
                p1, p2, = p2, p1
            else:
                p1 = p1.next
        return list1

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val <= list2.val:
            list1 = self.interleave_sorted(list1, list2)
            return list1
        else:
            list2 = self.interleave_sorted(list2, list1)
            return list2


def test_solution():

    def check_list_equivalence(actual_merged_list, expected_merged_list):
        while actual_merged_list and expected_merged_list:
            if actual_merged_list.val != expected_merged_list.val:
                return False
            actual_merged_list = actual_merged_list.next
            expected_merged_list = expected_merged_list.next

        return actual_merged_list is None and expected_merged_list is None

    def output_str_of_merged_list(merged_list):
        result_str = ""
        while merged_list.next:
            result_str = result_str + str(merged_list.val) + "->"
            merged_list = merged_list.next
        result_str += str(merged_list.val)
        return result_str

    s = Solution()

    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    expected_merged_list = ListNode(1)
    expected_merged_list.next = ListNode(1)
    expected_merged_list.next.next = ListNode(2)
    expected_merged_list.next.next.next = ListNode(3)
    expected_merged_list.next.next.next.next = ListNode(4)
    expected_merged_list.next.next.next.next.next = ListNode(4)

    actual_merged_list = s.mergeTwoLists(l1, l2)

    print("Expected result from input l1: 1->2->4 and l2: 1->3->4 is 1->1->2->3->4->4 and the Actual result is: " +
          output_str_of_merged_list(actual_merged_list))

    assert check_list_equivalence(
        actual_merged_list, expected_merged_list) == True


if __name__ == "__main__":
    test_solution()
