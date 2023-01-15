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


def SynchronizingTables(N: int, ids: List[int], salary: List[int]):
    """Gets the length of both arrays by the parameter N.
    The ids parameter is an array containing employee numbers,
    the salary parameter is an array containing salary.
    The function returns an array containing the reordered salary."""
    number_salary_dict = {}
    copy_ids = ids[:]
    copy_employee_salary = salary[:]
    # Copy both lists
    sort_salary = selectionSort(copy_employee_salary)
    sort_number = selectionSort(copy_ids)
    ordered_salary = []
    i = 0
    # Fills the dictionary with sorted values
    while i < len(sort_number):
        number_salary_dict[sort_number[i]] = sort_salary[i]
        i += 1

    # Searches from the list of numbers for a match in the dictionary by key,
    # and adds it to the ordered list of salary
    for i in range(len(ids)):
        for key, value in number_salary_dict.items():
            if ids[i] == key:
                ordered_salary.append(value)

    return ordered_salary
