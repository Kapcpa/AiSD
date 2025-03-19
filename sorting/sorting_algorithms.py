"""
TODO: 

plotting the complexity graphs, 

""" 


import random


def insertion_sort(array):
    for i in range(1, len(array)):  
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:  
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key


def shell_sort(array):
    gaps = [1, 5, 19, 41, 109, 209, 505, 929]  
    gaps = [g for g in gaps if g < len(array)]

    for gap in reversed(gaps):
        for i in range(gap, len(array)):
            temp = array[i]
            j = i

            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap

            array[j] = temp


def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:  
                min_index = j  
        array[i], array[min_index] = array[min_index], array[i]  


def make_heap(array, n, i):
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


def heap_sort(array):
    for i in range(len(array) // 2 - 1, -1, -1):
        make_heap(array, len(array), i)

    for i in range(len(array) - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        make_heap(array, i, 0)


def quick_sort_left(array, p=None, r=None):
    if p is None or r is None:
        p = 0
        r = len(array) - 1

    if p < r:
        q = partition(array, p, r)
        quick_sort_left(array, p, q - 1)
        quick_sort_left(array, q + 1, r)


def partition(array, p, r):
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


def quick_sort_rand(array, p=None, r=None):
    if p is None or r is None:
        p = 0
        r = len(array) - 1

    if p < r:
        q = partition_rand(array, p, r)
        quick_sort_rand(array, p, q - 1)
        quick_sort_rand(array, q + 1, r)


def partition_rand(array, p, r):
    """
    Idea is to reuse the partition_left to avoid writing more code
    so before we call partition() function we pick a random pivot and swap it with the first element
    
    """
    rand_pivot = random.randint(p, r)
    array[p], array[rand_pivot] = array[rand_pivot], array[p]
    return partition(array, p, r)  
