class Node:
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return str(self.val)


class Stack:
    def __init__(self, node=None):
        self.top = node
        if node:
            self.rest_of_stack = [node]
        else:
            self.rest_of_stack = []

    def __str__(self):
        result = []
        for n in self.rest_of_stack:
            result.append(str(n))
        return str(result)

    def push(self, node):
        self.top = node
        self.rest_of_stack.append(node)

    def is_empty(self):
        return self.rest_of_stack == []

    def pop(self):
        if not self.is_empty():
            result = self.rest_of_stack.pop()
            if self.is_empty():
                self.top = None
            else:
                self.top = self.rest_of_stack[-1]
            return result
        raise Exception('IndexError: pop from empty stack')

    def peek(self):
        return self.top


node3 = Node(3)
node2 = Node(2)
node1 = Node(1)
stack = Stack()
stack.push(node3)
print(stack)
stack.push(node2)
print(stack)
stack.push(node1)
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
print("peek called - top of stack is: " + str(stack.peek()))
print("stack empty? - "+str(stack.is_empty()))
print("Should throw error below:")
stack.pop()
