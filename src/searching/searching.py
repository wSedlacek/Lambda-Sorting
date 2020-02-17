# STRETCH: implement Linear Search
from typing import List


def linear_search(arr: List[int], target: int):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1


def binary_search(arr: List[int], target: int):
    if len(arr) == 0:
        return -1

    low = 0
    high = len(arr) - 1

    while low <= high:
        middle = (low + high) // 2

        if arr[middle] == target:
            return middle

        if arr[middle] < target:
            low += 1
        else:
            high -= 1

    return -1


def binary_search_recursive(arr: List[int], target: int, low: int = 0, high: int = None):
    if high is None:
        high = len(arr) - 1

    if len(arr) == 0 or low >= high:
        return -1

    middle = (low + high) // 2
    if arr[middle] == target:
        return middle

    if arr[middle] < target:
        return binary_search_recursive(arr, target, low + 1, high)

    else:
        return binary_search_recursive(arr, target, low, high - 1)
