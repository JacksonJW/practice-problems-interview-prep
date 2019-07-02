# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.


class MinStack(object):
    def __init__(self):
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.get_min() is None or x < self.get_min():
            self.stack.append((x, x))
        else:
            self.stack.append((x, self.get_min()))

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) > 0:
            return self.stack[-1][0]
        return None

    def get_min(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1][1]


# Tests:
min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
print('Should return -3: ' + str(min_stack.get_min()))
min_stack.pop()
print('Should return 0: ' + str(min_stack.top()))
print('Should return -2: ' + str(min_stack.get_min()))
