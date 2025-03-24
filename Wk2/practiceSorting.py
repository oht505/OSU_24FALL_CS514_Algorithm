def merge(A, l, mid, r):

    l_size = (mid-1)+1
    r_size = (r-mid)

    leftArray = [0] * l_size
    rightArray = [0] * r_size

    for i in range(0, l_size):
        leftArray[i] = A[l+i]

    for i in range(0, r_size):
        rightArray[i] = A[mid+1+i]

    i = 0
    j = 0
    k = 0

    while i < l_size and j < r_size:
        if leftArray[i] < rightArray[j]:
            A[k] = leftArray[i]
            i += 1
        else:
            A[k] = rightArray[j]
            j += 1
        k += 1

    while i < l_size:
        A[k] = leftArray[i]
        k += 1
        i += 1

    while j < r_size:
        A[k] = rightArray[j]
        k += 1
        j += 1
def mergeSort(A, l, r):
    if l < r:
        mid = (l + r) // 2
        mergeSort(A, l, mid)
        mergeSort(A, mid+1, r)
        merge(A, l, mid, r)

def partition(Arr, l , r):

    return 0
def quickSort(Arr, l, r):

    p = partition(Arr, l, r)

    quickSort(Arr, l, p-1)
    quickSort(Arr, p+1, r)

    return 0

if __name__ == "__main__":
    l = [7,2,5,4,3,1,8,6]
    # mergeSort(l, 0, (len(l)-1))
    # print(l)
    quickSort(l, 0, len(l)-1)
