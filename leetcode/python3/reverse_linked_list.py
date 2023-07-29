class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def turn_into_list(self):
        result = []
        ptr = self
        while ptr != None:
            result.append(ptr.val)
            ptr = ptr.next
        return result


def reverseList(head):
    def reverse(ptr, prev_ptr):
        if not ptr:
            return prev_ptr
        elif ptr.next == None:
            ptr.next = prev_ptr
            return ptr
        else:
            new_ptr = ptr.next.next
            ptr.next.next = ptr
            new_prev_ptr = ptr.next
            ptr.next = prev_ptr
            return reverse(new_ptr, new_prev_ptr)
    return reverse(head, None)


node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)
node.next.next.next.next = ListNode(5)

expected_linked_list = ListNode(5)
expected_linked_list.next = ListNode(4)
expected_linked_list.next.next = ListNode(3)
expected_linked_list.next.next.next = ListNode(2)
expected_linked_list.next.next.next.next = ListNode(1)

actual_linked_list = reverseList(node)
print("expected ist: " + str(expected_linked_list.turn_into_list()))
print("actual list: " + str(actual_linked_list.turn_into_list()))
