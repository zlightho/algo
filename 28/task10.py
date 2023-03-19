from typing import List


def MaximumDiscount(N: int, price: List[int]) -> int:
    """
    Calculates the maximum discount that can be obtained by buying items.

    Args:
        N: An integer representing the number of items in the store.
        price: A list of N integers representing the prices of the items.

    Returns:
        An integer representing the maximum discount that can be obtained
        by buying items in the store.
        The discount is calculated as the sum of every third item in the
        sorted list of prices.

    Example:
        >>> MaximumDiscount(7, [400, 350, 300, 250, 200, 150, 100])
        450
    """
    total_sum = sum(price)
    sorted_price = sorted(price, reverse=True)
    disc_price_list = sum(
        [sorted_price[i] for i in range(len(price)) if (i + 1) % 3 != 0]
    )
    return total_sum - disc_price_list
