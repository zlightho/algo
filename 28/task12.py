from typing import List


def MisterRobot(N: int, data: List[int]) -> bool:
    """
    This function checks if it is possible to sort a given list of integers
    from 1 to N using the following operation:
    Take any three consecutive elements in the list, and rotate them to the
    left any number of times.

    Args:
    N (int): The size of the list, and also the range of integers from 1 to N
    (inclusive). data (List[int]): The input list of integers from 1 to N.

    Returns:
    bool: True if it`s possible to sort the list using the specified operation,
    False otherwise.
    """

    for _ in range(N):
        for i in range(N - 2):
            if data[i] > data[i + 1]:
                data[i], data[i + 1], data[i + 2] = (
                    data[i + 1],
                    data[i + 2],
                    data[i],
                )

    return all(data[i] <= data[i + 1] for i in range(N - 1))
