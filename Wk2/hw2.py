## Homework Assignment Week 2: Divide and Conquer Algorithm,
##                             and Recurrence Relations
## Name: Hyuntaek Oh
## Email: ohhyun@oregonstate.edu
## Course: CS 514_400 Algorithms
## Due: Oct. 14, 2024
## Description: To implement rank_smallest function, I use
##              merge sorting to get sorted array. Then,
##              calculate ranks and print the elements.
#############################################################
import time
import numpy as np
import random
import matplotlib.pyplot as plt

def merge(left, right):
    ans = []
    i = j = 0

    # Merging the elements of left and right arrays
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            ans.append(left[i])
            i += 1
        else:
            ans.append(right[j])
            j += 1

    # Merging remaining elements
    ans += left[i:]
    ans += right[j:]

    return ans

def mergeSort(A):
    # Base case: only one element in the array
    if len(A) <= 1:
        return A

    # Mid-point for dividing
    mid = len(A) // 2

    # Merge left-sorted array and right-sorted array
    return merge(mergeSort(A[:mid]), mergeSort(A[mid:]))

def rank_smallest(A, b, k):

    ans = []

    # Print nothing
    if k == 0:
        return []

    # Sorting an array with merge sort
    sortedArray = mergeSort(A)

    # Print elements if the conditions are satisfied
    if k * b <= len(A):
        for i in range(0, k):
            ans.append(sortedArray[(b-1) + i*b])
    else:
        print(f"Warning: Should be k * b <= {len(A)}, "
              f"previous k * b was {k*b}.")
        return []

    return ans

def measuring_runtime(input_size, sorted=False):

    list = random.sample(range(0, 99999999), input_size)

    b = 5
    k = 10

    if sorted:
        list = mergeSort(list)

    start_time = time.time()
    rank_smallest(list, b, k)
    end_time = time.time()

    return end_time - start_time

# if __name__ == "__main__":
#     Arr = [7, 1, 4, 5, 2, 3, 6, 8, 9]
#     b = 3
#     k = 3
#
#     print("Sorted Array: ", mergeSort(Arr))
#     print("k: ", k, ", b: ", b)
#     print("Smallest rank: ", rank_smallest(Arr, b, k))
#
#     # Measuring runtime
#     input_size = [10**4, 5*(10**4), 10**5, 5*(10**5), 10**6, 5*(10**6), 10**7]
#     random_runtimes = []
#     sorted_runtimes = []
#
#     for size in input_size:
#         random_runtimes.append(measuring_runtime(size, False))
#         sorted_runtimes.append(measuring_runtime(size, True))
#
#     print("Randomly sorted runtimes: ", random_runtimes)
#     print("Already sorted runtimes: ", sorted_runtimes)
#
#     # Plotting
#     plt.figure(figsize=(10,6))
#     plt.plot(input_size, random_runtimes, label="Randomly sorted", color='red', marker="o")
#     plt.plot(input_size, sorted_runtimes, label="Already sorted", color='blue', marker="x")
#     plt.xlabel("Input size (n)")
#     plt.ylabel("Runtime (seconds)")
#     plt.title("Rank Smallest Algorithm Runtimes")
#     plt.legend()
#     plt.grid(True)
#     plt.xscale('log')
#     plt.yscale('log')
#     plt.show()
