def Keymaker(k: int) -> str:
    """
    Simulates the work of a keymaker who manipulates a series of doors.

    Args:
        k (int): The number of doors to simulate.

    Returns:
        str: A string of length k representing the state of each door after manipulation.

    Example:
        >>> Keymaker(10)
        '1110010000'
    """
    # Create a list of k boolean values representing the initial state of each door (all closed)
    doors = [False] * k

    # Simulate the keymaker's manipulations for each step
    for i in range(1, k + 1):
        for j in range(i - 1, k, i):
            doors[j] = not doors[j]

    # Convert the list of boolean values to a string of 1's and 0's representing the state of each door
    return "".join(str(int(door)) for door in doors)
