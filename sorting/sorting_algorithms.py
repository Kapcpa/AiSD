"""
TODO: 

quick sorts, shell sort, 

plotting the complexity graphs, 

""" 

def insertion_sort(array):
    for i in range(1, len(array)):  
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:  
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key


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