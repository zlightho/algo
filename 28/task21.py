from typing import List


def Football(F: List[int], N: int) -> bool:
    """
    Determines if an array of integers can be sorted in ascending order
    with a single application of one of two rules.

    Args:
        F (List[int]): A list of N integers.
        N (int): The length of the list F.

    Returns:
        bool: True if the list F can be sorted in ascending order
        with a single application of one of the following rules:
            1. Swap two arbitrary elements in the list.
            2. Reverse a subsequence of arbitrary length in the list.
        Otherwise, False.

    Examples:
        >>> Football([1, 3, 2], 3)
        True
        >>> Football([3, 2, 1], 3)
        True
        >>> Football([1, 7, 5, 3, 9], 5)
        True
        >>> Football([9, 5, 3, 7, 1], 5)
        False
        >>> Football([1, 4, 3, 2, 5], 5)
        True
    """
    if F == sorted(F):
        return False

    # rule1
    for i in range(N):
        for j in range(i + 1, N):
            new_F = F.copy()
            new_F[i], new_F[j] = new_F[j], new_F[i]
            if new_F == sorted(new_F):
                return True

    # rule2
    for i in range(N):
        for j in range(i + 1, N):
            new_F = F[:i] + F[i : j + 1][::-1] + F[j + 1 :]
            if new_F == sorted(new_F):
                return True

    return False
