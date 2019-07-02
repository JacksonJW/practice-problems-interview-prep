# Write a program to find the node at which the intersection of two singly linked lists begins.

# For example, the following two linked lists:

# [4, 1, 8, 4, 5]
# [5, 0, 1, 8, 4, 5]

# begin to intersect at node 8.


# The solution below has a time complextiy of O(n) and a space complexity of O(n)


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    ptr_a = headA
    ptr_b = headB
    visited_set = set()

    while ptr_a is not None:
        visited_set.add(ptr_a)
        ptr_a = ptr_a.next

    while ptr_b is not None:
        if ptr_b in visited_set:
            return ptr_b.val
        ptr_b = ptr_b.next

    return None


a = ListNode(4)
a.next = ListNode(1)
a.next.next = ListNode(8)
a.next.next.next = ListNode(4)
a.next.next.next.next = ListNode(5)

b = ListNode(5)
b.next = ListNode(0)
b.next.next = ListNode(1)
b.next.next.next = a.next.next
b.next.next.next.next = a.next.next.next
b.next.next.next.next.next = a.next.next.next.next

print('Should obtain an intersection at node with val 8: ' +
      str(getIntersectionNode(a, b)))
