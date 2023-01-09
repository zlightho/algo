from typing import List


def odometer(oksana: List[int]) -> int:
    """Get list with numbers, and return sum all elements with odd indices in the list"""
    dist = 0
    for i in range(len(oksana)):
        if i % 2 == 0:
            dist += oksana[i]
    return dist
