# Using array implementation to make a heap
class BinaryMaxHeap(object):
    def __init__(self, val):
        self.heap = [val]

    def __str__(self):
        return str(self.heap)

    def find_parent_position(self, child_position):
        if child_position == 0:
            return None
        if child_position % 2 == 1:
            return int(child_position / 2)
        return int((child_position / 2) - 1)

    def find_child_positions(self, parent_position):
        if (parent_position * 2) + 1 > len(self.heap)-1:
            return (None, None)
        elif (parent_position * 2) + 2 > len(self.heap)-1:
            return ((parent_position * 2) + 1, None)
        return (parent_position * 2) + 1, (parent_position * 2) + 2

    def insert(self, x):
        self.heap.append(x)
        x_pos = len(self.heap)-1
        parent_pos = self.find_parent_position(x_pos)

        while parent_pos is not None and x > self.heap[parent_pos]:
            self.heap[parent_pos], self.heap[x_pos] = self.heap[x_pos], self.heap[parent_pos]
            x_pos = parent_pos
            parent_pos = self.find_parent_position(x_pos)

    def extractMax(self):
        # 2. bubble down if root node is less than left then right (swap xs)
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        x = self.heap[0]
        x_pos = 0
        left_child_position, right_child_position = self.find_child_positions(
            x_pos)

        while left_child_position or right_child_position:
            if right_child_position and x < right_child_position and abs(self.heap[right_child_position] - x) >= abs(self.heap[left_child_position] - x):
                self.heap[x_pos], self.heap[right_child_position] = self.heap[right_child_position], self.heap[x_pos]
                x_pos = right_child_position
                left_child_position, right_child_position = self.find_child_positions(
                    x_pos)

            elif x < self.heap[left_child_position]:
                self.heap[x_pos], self.heap[left_child_position] = self.heap[left_child_position], self.heap[x_pos]
                x_pos = left_child_position
                left_child_position, right_child_position = self.find_child_positions(
                    x_pos)
            else:
                break

        return max_val

    def findMax(self):
        return self.heap[0]


heap = BinaryMaxHeap(5)
heap.insert(4)
heap.insert(6)
heap.insert(-1)
heap.insert(43)
print(heap)
heap.extractMax()
print(heap)
