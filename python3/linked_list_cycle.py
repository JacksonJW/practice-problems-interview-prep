class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head):
    if head is None or head.next is None:
        return False
    slow = head
    fast = head.next
    while fast is not slow:
        if fast is None or fast.next is None:
            return False
        slow = slow.next
        fast = fast.next.next
    return True


node = ListNode(3)
node.next = ListNode(2)
node.next.next = ListNode(0)
node.next.next.next = ListNode(-4)
node.next.next.next = node.next
assert hasCycle(node) == True
print('given [3,2,0,-4] with cycle at pos 1, should return true: ' +
      str(hasCycle(node)))

node1 = ListNode(1)
node1.next = ListNode(2)
node1.next.next = node
assert hasCycle(node1) == True
print('given [1,2] with cycle at pos 0, should return true: ' +
      str(hasCycle(node1)))

node2 = ListNode(1)
assert hasCycle(node2) == False
print('given [1,2] with cycle at pos 0, should return false: ' +
      str(hasCycle(node2)))
