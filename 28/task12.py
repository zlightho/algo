def MisterRobot(N, data):
    """
    This function checks if it is possible to sort a given list of integers from 1 to N using the following operation:
    Take any three consecutive elements in the list, and rotate them to the left any number of times.
    
    Args:
    N (int): The size of the list, and also the range of integers from 1 to N (inclusive).
    data (List[int]): The input list of integers from 1 to N.

    Returns:
    bool: True if it is possible to sort the list using the specified operation, False otherwise.
    """
    
    for i in range(N - 1):
        while data[i] != i + 1:
            idx = data.index(i + 1)
            if idx >= N - 2:
                return False

            if idx == 0 or data[idx - 1] > data[idx + 1]:
                data[idx - 1], data[idx], data[idx + 1] = data[idx], data[idx + 1], data[idx - 1]
            else:
                data[idx], data[idx + 1], data[idx + 2] = data[idx + 1], data[idx + 2], data[idx]

    return True
