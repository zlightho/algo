from typing import List


def find_smallest(arr):
    """Get array and return index of the smallest element"""
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
            assert i >= -1
    return smallest_index


def selectionSort(arr):
    """Get array and return sorted array"""
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


def MadMax(N: int, Tele: List[int]) -> List[int]:
    """"Get list Tele withe range N, and return impulse_list"""
    impulse_list = selectionSort(Tele)
    impulse_list[int(
        N/2-0.5)], impulse_list[-1] = impulse_list[-1],  impulse_list[int(N/2-0.5)]
    for i in range(int(N/2+0.5), N-1):
        impulse_list[i], impulse_list[i+1] = impulse_list[i+1], impulse_list[i]
    impulse_list[N-2], impulse_list[N-1] = impulse_list[N-1], impulse_list[N-2]
    return impulse_list