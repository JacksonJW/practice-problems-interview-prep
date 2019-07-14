# Queue - singly linked-list implementation for practice.
# Constant time O(1) add and removal from tail and head respectively.


class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None


class Queue:
    def __init__(self, val=None):
        if not val:
            self.head = None
            self.tail = None
        else:
            self.head = ListNode(val)
            self.tail = self.head

    def __str__(self):
        ptr = self.head
        result = []
        while ptr is not None:
            result.append(ptr.value)
            ptr = ptr.next
        return str(result)

    def peek(self):
        return self.head

    def is_empty(self):
        if self.head is None:
            return True
        return False

    def enqueue(self, val):
        if self.tail is None and self.head is None:
            self.head = ListNode(val)
            self.tail = self.head
        else:
            self.tail.next = ListNode(val)
            self.tail = self.tail.next

    def dequeue(self):
        if self.head is None and self.tail is None:
            return None
        if self.head is self.tail:
            self.tail = None
        result = self.head
        self.head = self.head.next
        return result


q = Queue()
print(q)
q.enqueue(5)
print(q)
q.enqueue(4)
print(q)
q.enqueue(3)
print(q)
q.enqueue(2)
print(q)
q.enqueue(1)
print(q)
q.dequeue()
print(q)
q.dequeue()
print(q)
q.dequeue()
print(q)
q.dequeue()
print(q)
q.dequeue()
print(q)
