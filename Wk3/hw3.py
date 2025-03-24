############################################################
## Homework Assignment Week 3: Sorting
## Name: Hyuntaek Oh
## Email: ohhyun@oregonstate.edu
## Course: CS 514_400 Algorithms
## Due: Oct. 21, 2024
#############################################################
import random
import time

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

def min_heapify(arr, n, i):
    smallest_idx = i
    left_idx = (2 * i) + 1
    right_idx = (2 * i) + 2

    # If left is larger than largest, assign it largest
    if left_idx < n and arr[left_idx] < arr[smallest_idx]:
        smallest_idx = left_idx

    # If right is larger than largest, assign it largest
    if right_idx < n and arr[right_idx] < arr[smallest_idx]:
        smallest_idx = right_idx

    # If changed, do max_heapify again
    if smallest_idx != i:
        arr[smallest_idx], arr[i] = arr[i], arr[smallest_idx]
        min_heapify(arr, n, smallest_idx)
def max_heapify(arr, n, i):
    largest_idx = i
    left_idx = (2 * i) + 1
    right_idx = (2 * i) + 2

    # If left is larger than largest, assign it largest
    if left_idx < n and arr[left_idx] > arr[largest_idx]:
        largest_idx = left_idx

    # If right is larger than largest, assign it largest
    if right_idx < n and arr[right_idx] > arr[largest_idx]:
        largest_idx = right_idx

    # If changed, do max_heapify again
    if largest_idx != i:
        arr[largest_idx], arr[i] = arr[i], arr[largest_idx]
        max_heapify(arr, n, largest_idx)

def heapSort(arr):

    # Length of input array
    n = len(arr)

    # Build Max-Heap
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

    # For sorting, repeat discarding process
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, i, 0)

    return arr

def measuring_runtime(input_size):

    long_list = random.sample(range(0, 99999999), input_size)
    sorted_list = sorted(long_list)
    reversed_list = sorted_list[::-1]

    start_time_list = time.time()
    heapSort(long_list)
    end_time_list = time.time()

    time_long_list = end_time_list - start_time_list

    start_time_sorted = time.time()
    heapSort(sorted_list)
    end_time_sorted = time.time()

    time_long_list_sorted = end_time_sorted - start_time_sorted

    start_time_reversed = time.time()
    heapSort(reversed_list)
    end_time_reversed = time.time()

    time_long_list_reversed = end_time_reversed - start_time_reversed

    return time_long_list, time_long_list_sorted, time_long_list_reversed

if __name__ == "__main__":
    l = [23,11,12,1,13,7,9,20]
    print("Sorted array is:", heapSort(l))

    # set_t1, set_t2, set_t3 = [], [], []
    # set_size = [x for x in range(3,7)]
    # print(set_size)
    # for size in set_size:
    #     t1, t2, t3 = measuring_runtime(10**(size))
    #     set_t1.append(t1)
    #     set_t2.append(t2)
    #     set_t3.append(t3)
    #
    # print("Real time taken in each case")
    # print(f"{'Input Size n':<20}{'Random List (s)':<25}{'Sorted List (s)':<25}{'Reverse Sorted List (s)'}")
    #
    # for i in range(len(set_size)):
    #     print(f'10^{set_size[i]:<20}{set_t1[i]:<25.6f}{set_t2[i]:<25.6f}{set_t3[i]:<25.6f}')
    #
    # print("long list time: ", t1)
    # print("sorted long list time: ", t2)
    # print("reversed long list time: ", t3)
