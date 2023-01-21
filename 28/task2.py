from typing import List


def SumOfThe(N: int, data: List[int]) -> int:
    """gets the length of the entire summary by the parameter N (N >= 2),
    and then the summary itself (integers) is stored in an array of length N.
    The function returns an integer from the summary,
    which is equal to the sum of all other numbers."""
    total = sum(data)
    for i in range(N):
        if total - data[i] == data[i]:
            return data[i]
    return None
