# Given a linked list, remove the n-th node
# from the end of list and return its head.

# Example:

# Given linked list: 1 -> 2 -> 3 -> 4 -> 5,
# and n = 2.

# After removing the second node from the end,
# the linked list becomes 1 -> 2 -> 3 -> 5.

# Note:
# Given n will always be valid.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def toList(self):
        result = []
        current_node = self
        while current_node != None:
            result.append(current_node.val)
            current_node = current_node.next
        return result


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    if n == 0:
        return head

    head_ptr = head
    current_node = head

    if current_node.next == None:
        return None

    while current_node.next != None:
        if findNthFromEnd(current_node.next, n) == "valid":
            current_node.next = current_node.next.next
            break
        elif findNthFromEnd(current_node.next, n) == "isHead":
            head_ptr = head_ptr.next
            break
        else:
            current_node = current_node.next

    return head_ptr


def findNthFromEnd(current_node, n) -> str:
    i = 0
    while i < n and current_node != None:
        current_node = current_node.next
        i += 1
    if i < n and current_node == None:
        return "isHead"
    elif current_node == None:
        return "valid"
    else:
        return "invalid"


node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)
node.next.next.next.next = ListNode(5)

resultNode = ListNode(1)
resultNode.next = ListNode(2)
resultNode.next.next = ListNode(4)
resultNode.next.next.next = ListNode(5)

print("result: " + str(removeNthFromEnd(node, 3).toList()))
print("result should be: " + str(resultNode.toList()))
