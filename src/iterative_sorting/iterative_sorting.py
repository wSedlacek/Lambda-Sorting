from typing import List


def swap(arr: List[int], index1: int, index2: int):
    arr[index1], arr[index2] = arr[index2], arr[index1]


def insertion_sort(arr: List[int]):
    if (len(arr) < 2):
        return arr

    first, *rest = arr
    sorted: List[int] = [first]
    for sorting in rest:
        sorted.insert(0, sorting)
        for i in range(0, len(sorted) - 1):
            if sorted[i] > sorted[i+1]:
                swap(sorted, i, i+1)
            else:
                break

    return sorted


def bubble_sort(arr: List[int]):
    first_run = True
    swap_occurred = False

    while first_run or swap_occurred:
        first_run = False
        swap_occurred = False

        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i+1]:
                swap(arr, i, i+1)
                swap_occurred = True
    return arr


def selection_sort(arr: List[int]):
    for cur_index in range(0, len(arr) - 1):
        smallest_index = cur_index
        for i in range(cur_index, len(arr)):
            if arr[i] < arr[smallest_index]:
                smallest_index = i

        swap(arr, cur_index, smallest_index)

    return arr


def count_sort(arr: List[int]):
    maximum = -1
    minimum = 0

    for item in arr:
        maximum = item if item > maximum else maximum
        minimum = item if item < minimum else minimum

    if minimum < 0:
        return 'Error, negative numbers not allowed in Count Sort'

    count = [0] * (maximum + 2)
    output = [0] * len(arr)

    for item in arr:
        count[item] += 1

    for index in range(len(count)):
        count[index] += count[index - 1]

    for index in range(len(arr)):
        current_val = arr[index]
        count[current_val] -= 1

        new_index = count[current_val]
        output[new_index] = current_val

    return output
