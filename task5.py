from typing import List

def find_smallest(arr: List):
    """Get array and return index of the smallest element"""
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
            assert i >= -1
    return smallest_index


def selectionSort(arr: List):
    """Get array and return sorted array"""
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


def SynchronizingTables(N: int, employee_numbers: List[int], salaries: List[int]):
    """Gets the length of both arrays by the parameter N.
    The ids parameter is an array containing employee numbers,
    the salary parameter is an array containing salaries.
    The function returns an array containing the reordered salaries."""
    number_salaries_dict = {}
    copy_employee_numbers = employee_numbers[:]
    copy_employee_salaries = salaries[:]
    # Copy both lists
    sort_salaries = selectionSort(copy_employee_salaries)
    sort_number = selectionSort(copy_employee_numbers)
    ordered_salaries = []
    i = 0
    # Fills the dictionary with sorted values
    while i < len(sort_number):
        number_salaries_dict[sort_number[i]] = sort_salaries[i]
        i += 1

    # Searches from the list of numbers for a match in the dictionary by key,
    # and adds it to the ordered list of salaries
    for i in range(len(employee_numbers)):
        for key, value in number_salaries_dict.items():
            if employee_numbers[i] == key:
                ordered_salaries.append(value)

    return ordered_salaries
