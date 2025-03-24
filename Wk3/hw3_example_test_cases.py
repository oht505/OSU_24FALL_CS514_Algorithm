class minPriorityQueue:
    def __init__(self):
        self.minHeap = []

    def min_heapify(self, idx):
        smallest = idx
        left = (2 * idx) + 1
        right = (2 * idx) + 2

        if left < len(self.minHeap) and self.minHeap[left] < self.minHeap[smallest]:
            smallest = left

        if right < len(self.minHeap) and self.minHeap[right] < self.minHeap[smallest]:
            smallest = right

        if smallest != idx:
            self.minHeap[idx], self.minHeap[smallest] = self.minHeap[smallest], self.minHeap[idx]
            self.min_heapify(smallest)

    def insert(self, val):
        self.minHeap.append(val)
        if self.minHeap:
            for idx in range(len(self.minHeap) // 2 - 1, -1, -1):
                self.min_heapify(idx)

    def first(self):
        if self.minHeap:
            return self.minHeap[0]
        else:
            return None

    def remove_first(self):
        if len(self.minHeap) == 0:
            return None

        lowest = self.first()
        self.minHeap[0] = self.minHeap[-1]
        self.minHeap.pop()

        n = len(self.minHeap)

        if self.minHeap:
            for idx in range(n // 2 - 1, -1, -1):
                self.min_heapify(idx)

        return lowest
def test_MinPriorityQueue():
    # Test case 1: Basic functionality
    priority_queue1 = minPriorityQueue()
    priority_queue1.insert(5)
    priority_queue1.insert(1)
    priority_queue1.insert(7)
    priority_queue1.insert(3)

    assert priority_queue1.first() == 1, f"Expected 1 but found {priority_queue1.first()}"
    assert priority_queue1.remove_first() == 1, f"Expected 1 but found {priority_queue1.remove_first()}"
    assert priority_queue1.first() == 3, f"Expected 3 but found {priority_queue1.first()}"

    # Test case 2: Inserting in sorted order
    priority_queue2 = minPriorityQueue()
    for i in range(5):
        priority_queue2.insert(i)
    assert priority_queue2.first() == 0, f"Expected 0 but found {priority_queue2.first()}"
    assert priority_queue2.remove_first() == 0, f"Expected 0 but found {priority_queue2.remove_first()}"

    # Test case 3: Inserting in reverse order
    priority_queue3 = minPriorityQueue()
    for i in range(4, -1, -1):
        priority_queue3.insert(i)
    assert priority_queue3.first() == 0, f"Expected 0 but found {priority_queue3.first()}"

    # Test case 4: Removing until empty
    priority_queue4 = minPriorityQueue()
    values = [8, 2, 6, 4, 10]
    for v in values:
        priority_queue4.insert(v)
    sorted_values = sorted(values)
    for v in sorted_values:
        assert priority_queue4.remove_first() == v, f"Expected {v} but got a different value"

    assert priority_queue4.first() is None, f"Expected None but got {priority_queue4.first()}"
    assert priority_queue4.remove_first() is None, f"Expected None but got {priority_queue4.remove_first()}"

    # Test case 5: Inserting duplicate values
    priority_queue5 = minPriorityQueue()
    for v in [3, 1, 4, 1, 5, 1]:
        priority_queue5.insert(v)
    expected_order = [1, 1, 1, 3, 4, 5]
    for v in expected_order:
        assert priority_queue5.remove_first() == v, f"Expected {v} but got a different value"

    # Test case 6: Edge case of an empty priority queue
    priority_queue6 = minPriorityQueue()
    assert priority_queue6.first() is None, f"Expected None but got {priority_queue6.first()}"
    assert priority_queue6.remove_first() is None, f"Expected None but got {priority_queue6.remove_first()}"

    # Test case 7: Single element
    priority_queue7 = minPriorityQueue()
    priority_queue7.insert(5)
    assert priority_queue7.first() == 5, f"Expected 5 but got {priority_queue7.first()}"
    assert priority_queue7.remove_first() == 5, f"Expected 5 but got {priority_queue7.remove_first()}"
    assert priority_queue7.first() is None, f"Expected None but got {priority_queue7.first()}"

    # Test case 8: Multiple elements, including negatives
    priority_queue8 = minPriorityQueue()
    for v in [-2, -1, 0, 1, 2]:
        priority_queue8.insert(v)
    assert priority_queue8.remove_first() == -2, f"Expected -2 but got a different value"
    assert priority_queue8.remove_first() == -1, f"Expected -1 but got a different value"

    print("All tests passed for minPriorityQueue!")

test_MinPriorityQueue()