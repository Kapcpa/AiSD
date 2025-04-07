import random


def insertion_sort(array: list[int], gap: int = 1):
    for i in range(gap, len(array)):
        temp = array[i]
        j = i

        while j >= gap and array[j - gap] > temp:
            array[j] = array[j - gap]
            j -= gap

        array[j] = temp


def shell_sort(array: list[int]):
    gaps = [1]
    k = 0
    while gaps[-1] < len(array) // 2:
        gaps.append(4 ** (k + 1) + 3 * (2 ** k) + 1)  # computing sedgewick's gaps
        k += 1

    for gap in reversed(gaps):
        insertion_sort(array, gap)


def selection_sort(array: list[int]):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:  
                min_index = j  
        array[i], array[min_index] = array[min_index], array[i]  


def make_heap(array: list[int], n: int, i: int):
    largest = i
    left = 2 * i + 1  
    right = 2 * i + 2  

    if left < n and array[left] > array[largest]:
        largest = left

    if right < n and array[right] > array[largest]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        make_heap(array, n, largest)


def heap_sort(array: list[int]):
    for i in range(len(array) // 2 - 1, -1, -1):
        make_heap(array, len(array), i)

    for i in range(len(array) - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        make_heap(array, i, 0)


#def quick_sort_left(...):
#    def pivot_left(arr):
#        return arr[0]
#    quick_sort(..., pivot_left)
#    quick_sort(..., lambda arr : arr[0])

#def quick_sort(..., pivot_f):
#    ...
#    pivot = pivot_f(...)
#    ...


def quick_sort_left(array: list[int], p: int | None = None, r: int | None = None):
    if p is None or r is None:
        p = 0
        r = len(array) - 1

    while p < r:
        q = partition(array, p, r)

        if q - p < r - q:
            quick_sort_left(array, p, q - 1)
            p = q + 1
        else:
            quick_sort_left(array, q + 1, r)
            r = q - 1


def partition(array: list[int], p: int, r: int):
    pivot = array[p]
    i = p + 1
    j = r  

    while True:
        while i <= j and array[i] <= pivot:  
            i += 1
        while i <= j and array[j] > pivot:  
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
        else:
            break

    array[p], array[j] = array[j], array[p]
    return j


def quick_sort_rand(array: list[int], p: int | None = None, r: int | None = None):
    if p is None or r is None:
        p = 0
        r = len(array) - 1

    if p < r:
        q = partition_rand(array, p, r)
        quick_sort_rand(array, p, q - 1)
        quick_sort_rand(array, q + 1, r)


def partition_rand(array: list[int], p: int, r: int):
    """
    Idea is to reuse the partition_left to avoid writing more code
    so before we call partition() function we pick a random pivot and swap it with the first element
    
    """
    rand_pivot = random.randint(p, r)
    array[p], array[rand_pivot] = array[rand_pivot], array[p]
    return partition(array, p, r)  
