from math import ceil
from typing import List


def quick_sort(arr: List[int]):
    if not arr:
        return arr

    pivot = arr[0]
    below = [num for num in arr[1:] if num < pivot]
    above = [num for num in arr[1:] if num >= pivot]
    return [*quick_sort(below), pivot, *quick_sort(above)]


def split(arr: List[int]):
    half_length = ceil(len(arr) / 2)
    return arr[:half_length], arr[half_length:]


def merge(left: List[int], right: List[int]):
    if not left:
        return right

    if not right:
        return left

    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)
    else:
        return [right[0]] + merge(left, right[1:])


def merge_sort(arr: List[int]):
    if len(arr) > 1:
        half1, half2 = split(arr)
        sorted1 = merge_sort(half1)
        sorted2 = merge_sort(half2)
        arr = merge(sorted1, sorted2)

    return arr


#################################################

def split_index(left: int, right: int):
    return ceil(left + right)


def swap(arr: List[int], index1: int, index2: int):
    arr[index1], arr[index2] = arr[index2], arr[index1]


def merge_in_place(arr: List[int], left: int, mid: int, right: int):
    pass


def merge_sort_in_place(arr: List[int], left: int, right: int):
    if left - right > 1:
        mid = split_index(left, right)
        merge_sort_in_place(arr, left, mid)
        merge_sort_in_place(arr, mid, right)
        merge_in_place(arr, left, mid, right)


#################################################


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    pass
