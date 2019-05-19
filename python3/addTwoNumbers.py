# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def print(self):
        result = []
        while self != None:
            result.append(self.val)
            self = self.next
        return str(result)


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    l1_strbuilder = ""
    l2_strbuilder = ""

    while l1 != None:
        l1_strbuilder = str(l1.val) + l1_strbuilder
        l1 = l1.next
    while l2 != None:
        l2_strbuilder = str(l2.val) + l2_strbuilder
        l2 = l2.next

    str_sum = str(int(l1_strbuilder) + int(l2_strbuilder))
    resultNode = ListNode(0)
    pointerNode = resultNode

    for i in reversed(range(len(str_sum))):
        pointerNode.val = int(str_sum[i])
        if i > 0:
            pointerNode.next = ListNode(0)
            pointerNode = pointerNode.next
    return resultNode


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

expected = ListNode(7)
expected.next = ListNode(0)
expected.next.next = ListNode(8)

print("expected: "+expected.print())
print("outcome: "+addTwoNumbers(l1, l2).print())

assert(addTwoNumbers(l1, l2).print() == expected.print())
